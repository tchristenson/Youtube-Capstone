import React, { useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import styles from './NewPlaylistModal.module.css'
import { useModal } from '../../context/Modal';
import { createPlaylistThunk } from "../../store/playlists";
import { addOrRemoveVideoFromPlaylistThunk } from "../../store/playlists";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function NewPlaylistModal({video, allPlaylistsArr}) {

    const dispatch = useDispatch()
    const { closeModal } = useModal();
    const sessionUser = useSelector(state => state.session.user)

    const [playlistName, setPlaylistName] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);
    const [showForm, setShowForm] = useState(false)
    const [selectedPlaylists, setSelectedPlaylists] = useState([]);

    console.log('video inside NewPlaylistModal', video)
    console.log('sessionUser inside NewPlaylistModal', sessionUser)
    console.log('allPlaylistsArr inside of NewPlaylistModal', allPlaylistsArr)

    const handlePlaylistSelection = (e, playlist) => {
        const playlistId = e.target.value
        if (sessionUser) {
            dispatch(addOrRemoveVideoFromPlaylistThunk(video.id, playlistId))
            if (e.target.checked) {
                setSelectedPlaylists((prevSelectedPlaylists) => [...prevSelectedPlaylists, playlistId]);
                toast(`Video added to ${playlist.name}`);
              } else {
                setSelectedPlaylists((prevSelectedPlaylists) =>
                  prevSelectedPlaylists.filter((id) => id !== playlistId)
                );
                toast(`Video removed from ${playlist.name}`);
              }
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)

        const formData = new FormData()
        if (validationErrors.length) return alert('Playlist name cannot exceed 100 characters')

        formData.append('name', playlistName.trim())
        formData.append('id', video.id)

        await dispatch(createPlaylistThunk(formData))

        setPlaylistName('')
        setHasSubmitted(false)
        setValidationErrors([])

        closeModal()
    }

    useEffect(() => {
        const errors = [];
        if (!playlistName.trim()) errors.push('Playlist name cannot be empty')
        if (playlistName.trim().length > 100) errors.push('Playlist name cannot exceed 100 characters')
        setValidationErrors(errors)
    }, [playlistName])

    const showFormToggle = () => {
        showForm? setShowForm(false) : setShowForm(true)
    }

    const sessionUserPlaylists = allPlaylistsArr.filter(playlist => playlist.userId === sessionUser.id)
    console.log('sessionUserPlaylists', sessionUserPlaylists)

    const filteredSessionUserPlaylists = sessionUserPlaylists.filter(playlist => {
        return !playlist.videos.some(currVideo => currVideo.id === video.id)
    })

    // console.log('filteredSessionUserPlaylists', filteredSessionUserPlaylists)

    const selectablePlaylists = filteredSessionUserPlaylists.map(playlist => (
        <div key={playlist.id} className={styles["user-playlists"]}>
            <label>
                <input
                    type="checkbox"
                    name={playlist.name}
                    value={playlist.id}
                    onChange={(e) => handlePlaylistSelection(e, playlist)}
                />
            {playlist.name}
            </label>
        </div>
    ))

    return (
        <div className={styles["new-playlist-form"]}>
            <ToastContainer />
            {selectablePlaylists.length? (
                <>
                    <h4 className={styles["header"]}>Save to...</h4>
                        <div className={styles["playlists-container"]}>
                            {selectablePlaylists}
                        </div>
                </>
            ) : (
                <h5 className={styles["no-playlists-message"]}>No playlists currently available</h5>
            )
            }
            <div className={styles["buttons-container"]}>
                <div onClick={showFormToggle} className={styles["new-playlist-button-container"]}>
                    <i id={styles['playlist-plus']} className="fa-solid fa-plus"></i>
                    <button className={styles['new-playlist-button']}>
                        Create New Playlist
                    </button>
                </div>
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
