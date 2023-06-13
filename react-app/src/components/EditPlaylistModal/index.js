import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { editPlaylistThunk } from "../../store/playlists";
import { useModal } from "../../context/Modal";
import styles from './EditPlaylistModal.module.css'



function EditPlaylistModal({playlist}) {

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    const [name, setName] = useState(playlist.name)
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    const handleSubmit = async (e) => {
        console.log('handleSubmit running')
        e.preventDefault();

        setHasSubmitted(true)
        if (validationErrors.length) return alert('Playlist cannot exceed 100 characters')

        const formData = new FormData()

        formData.append('name', name)
        formData.append('id', playlist.id)

        for (let key of formData.entries()) {
            console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
          }

        await dispatch(editPlaylistThunk(formData))

        setName('')
        setHasSubmitted(false)
        setValidationErrors([])
        closeModal()
    }

    useEffect(() => {
        const errors = [];
        if (!name) errors.push('Playlist name cannot be empty')
        if (name.length > 100) errors.push('Playlist name cannot exceed 100 characters')
        setValidationErrors(errors)
    }, [name])

    return (
        <div className={styles['playlist-container']}>
            <h2 className={styles["header"]}>Edit your playlist's name</h2>
            <form
                onSubmit={(e) => handleSubmit(e)}
            >
                <div className={styles["input"]}>
                    <input
                        type="text"
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                        >
                    </input>
                </div>

                <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={(e) => {
                    e.preventDefault(); setName(''); closeModal() }}
                    type="submit">Cancel</button>
                <button
                    className={name ? styles['submit-button-active'] : styles['submit-button']}
                    disabled={name ? false : true}
                    type="submit">Save</button>
            </div>
            </form>
        </div>
    )
}

export default EditPlaylistModal
