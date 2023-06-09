import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";

import styles from './DeletePlaylistModal.module.css'

function DeletePlaylistModal({playlist}) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault()

        // const deletedPlaylist = await dispatch(deleteCommentThunk(comment.id)) // Change this to deletePlaylistThunk
        // if (deletedPlaylist.message === 'delete successful') {
        //     closeModal() // Don't want to redirect user if possible - user will be deleting video's from their profile page, so
        //     // their page should just updated with the deleted video gone
        // }
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
