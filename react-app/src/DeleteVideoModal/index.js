import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { useModal } from "../context/Modal";
import { deleteVideoThunk } from "../store/videos";


function DeleteVideoModal({videoId}) {
    const dispatch = useDispatch();
    const history = useHistory();

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
        <div>
            <h1 className="modalText">Delete forever</h1>
            <form onSubmit={handleDelete}>
                <button type="submit">Delete</button>
                <button onClick={closeModal}>Cancel</button>
            </form>
        </div>

    )

}

    export default DeleteVideoModal
