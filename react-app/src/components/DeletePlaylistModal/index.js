import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { deletePlaylistThunk } from "../../store/playlists";
import styles from './DeletePlaylistModal.module.css'
import { useHistory } from "react-router-dom";

function DeletePlaylistModal({playlist}) {
    const dispatch = useDispatch();
    const history = useHistory();

    const sessionUser = useSelector(state => state.session.user)

    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault()
        console.log('handleDelete running')

        const deletedPlaylist = await dispatch(deletePlaylistThunk(playlist.id))
        if (deletedPlaylist.message === 'delete successful') {
            closeModal()
        }
        history.push(`/users/${sessionUser.id}`)
    }

    return (
        <div className={styles['delete-playlist-modal']}>
            <h2 className={styles["header"]}>Delete forever?</h2>
            <form onSubmit={handleDelete}>
            <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={closeModal}>Cancel</button>
                <button className={styles['submit-button-active']} type="submit">Delete</button>
            </div>
            </form>
        </div>
    )

}

export default DeletePlaylistModal
