import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import styles from './NewPlaylistModal.module.css'
import { useModal } from '../../context/Modal';
import { createPlaylistThunk } from "../../store/playlists";

function NewPlaylistModal({video}) {

    const dispatch = useDispatch()
    const { closeModal } = useModal();
    const sessionUser = useSelector(state => state.session.user)

    const [playlistName, setPlaylistName] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);
    const [showForm, setShowForm] = useState(false)

    console.log('video inside NewPlaylistModal', video)
    console.log('sessionUser inside NewPlaylistModal', sessionUser)

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)

        const formData = new FormData()
        if (validationErrors.length) return alert('Playlist name cannot exceed 100 characters')

        formData.append('name', playlistName.trim())

        await dispatch(createPlaylistThunk(formData))

        setPlaylistName('')
        setHasSubmitted(false)
        setValidationErrors([])
    }

    useEffect(() => {
        const errors = [];
        if (!playlistName.trim()) errors.push('Playlist name cannot be empty')
        if (playlistName.trim().length > 100) errors.push('Playlist name cannot exceed 100 characters')
        setValidationErrors(errors)
    }, [playlistName])

    const showFormToggle = () => {
        console.log('is this working')

        setShowForm(true)
    }


    return (
        <div className={styles["new-playlist-form"]}>
            <h4 className={styles["header"]}>Save to...</h4>
            <div className={styles["new-playlist-button-container"]}>
                <i id={styles['playlist-plus']} className="fa-solid fa-plus"></i>
                <button onClick={showFormToggle} className={styles['new-playlist-button']}>
                    Create New Playlist
                </button>
                {showForm &&
                    <form
                        onSubmit={(e) => handleSubmit(e)}
                    >
                        <div>
                            <input
                                className={styles['playlist-input-box']}
                                type="text"
                                onChange={(e) => setPlaylistName(e.target.value)}
                                value={playlistName}
                                placeholder="Enter playlist name..."
                                >
                            </input>
                        </div>
                        <div className={styles['buttons']}>
                            <button className={styles['cancel-button']} onClick={(e) => { e.preventDefault(); setPlaylistName(''); closeModal()}} type="submit">Cancel</button>
                            <button className={playlistName.trim() ? styles['submit-button-active'] : styles['submit-button']} disabled={playlistName.trim() ? false : true} type="submit">Create</button>
                        </div>
                    </form>
                }
            </div>

        </div>
    )

}

export default NewPlaylistModal
