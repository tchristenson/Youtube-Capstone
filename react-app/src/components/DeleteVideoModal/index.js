import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteVideoThunk } from "../../store/videos";
import styles from './DeleteVideoModal.module.css'


function DeleteVideoModal({videoId}) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault()

        const deletedVideo = await dispatch(deleteVideoThunk(videoId))
        if (deletedVideo.message === 'delete successful') {
            closeModal() // Don't want to redirect user if possible - user will be deleting video's from their profile page, so
            // their page should just updated with the deleted video gone
        }
    }

    return (
        <div className={styles['delete-video-form']}>
            <h1 className="modalText">Delete forever</h1>
            <form onSubmit={handleDelete}>
                <button type="submit">Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </form>
        </div>

    )

}

    export default DeleteVideoModal
