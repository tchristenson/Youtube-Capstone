import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteCommentThunk } from "../../store/comments";
import styles from './DeleteCommentModal.module.css'

function DeleteCommentModal({comment}) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault()

        const deletedComment = await dispatch(deleteCommentThunk(comment.id)) // Change this to deleteCommentThunk
        if (deletedComment.message === 'delete successful') {
            closeModal() // Don't want to redirect user if possible - user will be deleting video's from their profile page, so
            // their page should just updated with the deleted video gone
        }
    }

    return (
        <div className={styles['delete-comment-modal']}>
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

    export default DeleteCommentModal
