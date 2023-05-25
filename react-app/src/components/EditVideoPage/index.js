import React, { useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { editVideoThunk } from "../../store/videos";
import { getSingleVideoThunk } from "../../store/videos";
import styles from './EditVideoPage.module.css'
import { useModal } from '../../context/Modal';


function EditVideoPage({video}) {

    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal();
    // const {videoId} = useParams()

    const sessionUser = useSelector(state => state.session.user)
    // const video = useSelector(state => state.videos[videoId])

    // useEffect(() => {
    //     dispatch(getSingleVideoThunk(videoId))
    // }, [dispatch, videoId])

    useEffect(() => {
        if (video) {
            if (!sessionUser || sessionUser.id !== video?.userId) {
              history.push('/')
            }
        }
      }, [sessionUser, history, video])

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

        closeModal()

        // history.push(`/videos/${editedVideo.id}`)
    }

    useEffect(() => {
        const errors = [];
        // Only adding to the validation errors for fields that are nullable=False in the Video model
        if (!name) errors.push('Videos require a name')
        if (name.length > 100) errors.push('Video name must be 100 characters or fewer')
        if (description.length > 500) errors.push('Video description must be 500 characters or fewer')
        if (!thumbnail) errors.push('Please provide a thumbnail image file')
        setValidationErrors(errors)
    }, [name, description, thumbnail])

    return (
        <div className={styles['edit-video-form']}>
            <h2 className={styles["header"]}>Video details</h2>
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
                <div className={styles["input"]}>
                    <label>{'Title (required)'}</label>
                    <input
                        type="text"
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                        required={true}
                        >
                    </input>
                </div>

                <div className={styles["input"]}>
                    <label>Description</label>
                    <textarea
                        onChange={(e) => setDescription(e.target.value)}
                        value={description}
                        >
                    </textarea>
                </div>

                <div className={styles["thumbnail"]}>
                    <label>{`Thumbnail (required):`}</label>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={(e) => setThumbnail(e.target.files[0])}
                        required={true}
                        >
                    </input>
                </div>

                <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={(e) => {
                    e.preventDefault(); setDescription(''); setName(''); setThumbnail(''); closeModal() }}
                    type="submit">Cancel</button>
                <button
                    className={name && thumbnail ? styles['submit-button-active'] : styles['submit-button']}
                    disabled={name && thumbnail? false : true}
                    type="submit">Save</button>

            </div>

            </form>
        </div>
    )
}

export default EditVideoPage
