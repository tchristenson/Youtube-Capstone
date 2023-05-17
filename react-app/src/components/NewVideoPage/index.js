import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { uploadVideoThunk } from "../../store/videos";

function NewVideoPage() {

    const dispatch = useDispatch()
    const history = useHistory()

    const sessionUser = useSelector(state => state.session.user)

    useEffect(() => {
        if (!sessionUser) {
          history.push('/')
        }
      }, [sessionUser, history])

    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [content, setContent] = useState('');
    const [thumbnail, setThumbnail] = useState('');
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [files, setFiles] = useState([])
    const inputRef = useRef()

    const handleDragOver = (e) => {
        e.preventDefault()
      }

      const handleDrop = (e) => {
        e.preventDefault()
        const droppedFiles = e.dataTransfer.files
        if (droppedFiles.length) setContent(droppedFiles[0])

        // console.log('files state var', files)
        let currFileNames = []
        if (files.length) {
            files.forEach(file => currFileNames.push(file.name))
        }

        // console.log('currFileNames', currFileNames)
        // console.log('e.dataTransfer.files', e.dataTransfer.files)
        // console.log('e.dataTransfer.files[0]', e.dataTransfer.files[0])

        let filesArr = Object.values(e.dataTransfer.files)
        filesArr = filesArr.filter(file => !currFileNames.includes(file.name))
        // console.log('filesArr', filesArr)
        setFiles((prevFiles) => [...prevFiles, ...filesArr])
        // console.log('files state var', files)

      }

      const handleCancel = (canceledFile) => {
        setFiles((prevFiles) => {
          const filteredFiles = Array.from(prevFiles).filter((file) => file !== canceledFile);
          return filteredFiles.length === 0 ? [] : filteredFiles;
        });
      };

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)
        if (validationErrors.length) return alert('Your Post has errors, cannot submit!')

        const formData = new FormData()
        formData.append('name', name)
        formData.append('description', description)
        formData.append('content', content)
        formData.append('thumbnail', thumbnail)

        for (let key of formData.entries()) {
              console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
            }

        const newVideo = await dispatch(uploadVideoThunk(formData))

        setName('')
        setDescription('')
        setContent('')
        setThumbnail('')
        setValidationErrors([])
        setHasSubmitted(false)
        setFiles([])

        history.push(`/videos/${newVideo.id}`)
    }

    useEffect(() => {
        const errors = [];
        // Only adding to the validation errors for fields that are nullable=False in the Video model
        if (!name) errors.push('Videos require a name')
        if (!content) errors.push('Please provide a video file')
        if (!thumbnail) errors.push('Please provide a thumbnail image file')
        setValidationErrors(errors)
    }, [name, content, thumbnail])

    return (
        <div className="new-video-form">
            <h2 className="form-header">Upload videos</h2>
            {hasSubmitted && validationErrors.length > 0 && (
                <div>
                    <h2>The following errors were found:</h2>
                    <ul>
                        {validationErrors.map(error => (
                            <li key={error}>{error}</li>
                        ))}
                    </ul>
                </div>
            )}
            <form
                onSubmit={(e) => handleSubmit(e)}
                encType="multipart/form-data"
            >
                <div>
                    <label>{'Title (required)'}</label>
                    <input
                        type="text"
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                        required={true}
                        >
                    </input>
                </div>

                <div>
                    <label>Description</label>
                    <input
                        type="textarea"
                        onChange={(e) => setDescription(e.target.value)}
                        value={description}
                        >
                    </input>
                </div>

                <div>
                    <label>Thumbnail</label>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={(e) => setThumbnail(e.target.files[0])}
                        required={true}
                        >
                    </input>
                </div>

                <div>
                    {files && (
                        <>
                        <div className="uploads">
                            <ul>
                            {Array.from(files).map((file, idx) =>
                                <li key={idx}>
                                {file.name}
                                <button className="cancel-song" onClick={() => handleCancel(file)}>Cancel</button>
                                </li>)}
                            </ul>
                        </div>
                        </>
                    )}

                    <div
                    className="dropzone"
                    onDragOver={handleDragOver}
                    onDrop={handleDrop}
                    >

                    <label className="dropdown-text">Drag and drop video files to upload</label>
                    <input
                        type="file"
                        accept="video/*"
                        // onChange={(e) => setContent(e.target.files[0])}
                        hidden
                        ref={inputRef}
                    />
                    </div>

                </div>

                <button type="submit">Upload Video</button>

            </form>


        </div>

    )

}

export default NewVideoPage