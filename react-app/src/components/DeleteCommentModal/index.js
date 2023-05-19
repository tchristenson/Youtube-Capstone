import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { deleteCommentThunk } from "../../store/comments";


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
        <div>
            <h1 className="modalText">Delete forever</h1>
            <form onSubmit={handleDelete}>
                <button type="submit">Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </form>
        </div>

    )

}

    export default DeleteCommentModal
