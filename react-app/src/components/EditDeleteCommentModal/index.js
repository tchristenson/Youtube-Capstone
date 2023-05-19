import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import DeleteCommentModal from "../DeleteCommentModal";
import './EditDeleteCommentModal.css'



function EditDeleteCommentModal({comment}) {
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    const handleEdit = async (e) => {
        e.preventDefault()


    }

    return (
        <>
        {sessionUser.id === comment.userId && (
            <div>
                <form onSubmit={handleEdit}>
                    <button onClick={closeModal} type="submit">Edit</button>
                </form>
                <OpenModalButton buttonText='Delete' modalComponent={<DeleteCommentModal comment={comment}/>}></OpenModalButton>
            </div>
        )}

        {sessionUser.id !== comment.userId && (
            <div>
                <button className="unauthorized-icon" onClick={closeModal}>Report</button>
            </div>
        )}


        </>
    )
}

export default EditDeleteCommentModal
