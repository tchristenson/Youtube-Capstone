import React, { useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { editVideoThunk } from "../../store/videos";
import { getSingleVideoThunk } from "../../store/videos";


function EditVideoPage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {videoId} = useParams()

    const sessionUser = useSelector(state => state.session.user)
    const video = useSelector(state => state.videos[videoId])

    useEffect(() => {
        dispatch(getSingleVideoThunk(videoId))
    }, [dispatch, videoId])

    useEffect(() => {
        if (video) {
            if (!sessionUser || sessionUser.id !== video?.userId) {
              history.push('/')
            }
        }
      }, [sessionUser, history, video, videoId])

    useEffect(() => {
        if (video) {
            setName(video.name)
            setDescription(video.description)
        }
    }, [video])

    const [name, setName] = useState(video ? video.name : '');
    const [description, setDescription] = useState(video ? video.description : '');
    const [thumbnail, setThumbnail] = useState('');
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)
        if (validationErrors.length) return alert('Your Post has errors, cannot submit!')

        const formData = new FormData()
        formData.append('name', name)
        formData.append('description', description)
        formData.append('thumbnail', thumbnail)
        formData.append('id', video.id)

        for (let key of formData.entries()) {
              console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
            }

        const editedVideo = await dispatch(editVideoThunk(formData))

        setName('')
        setDescription('')
        setThumbnail('')
        setValidationErrors([])
        setHasSubmitted(false)

        history.push(`/videos/${editedVideo.id}`)
    }

    useEffect(() => {
        const errors = [];
        // Only adding to the validation errors for fields that are nullable=False in the Video model
        if (!name) errors.push('Videos require a name')
        if (!thumbnail) errors.push('Please provide a thumbnail image file')
        setValidationErrors(errors)
    }, [name, thumbnail])

    return (
        <div className="edit-video-form">
            <h2 className="form-header">Video details</h2>
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

                <button type="submit">Save</button>

            </form>
        </div>
    )
}

export default EditVideoPage
