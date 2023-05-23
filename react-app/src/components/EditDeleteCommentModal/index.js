import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import DeleteCommentModal from "../DeleteCommentModal";
import EditCommentModal from "../EditCommentModal";
import styles from './EditDeleteCommentModal.module.css'



function EditDeleteCommentModal({comment}) {
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    const handleEdit = async (e) => {
        e.preventDefault()


    }

    return (
        <>
            {sessionUser && sessionUser.id === comment.userId && (

                <div className={styles['buttons-container']}>

                    <OpenModalButton buttonText='Edit' modalComponent={<EditCommentModal comment={comment}/>}></OpenModalButton>
                    <OpenModalButton buttonText='Delete' modalComponent={<DeleteCommentModal comment={comment}/>}></OpenModalButton>

                </div>


            )}
            {sessionUser && sessionUser.id !== comment.userId && (
                <div>
                    <button className={styles['unauthorized-icon']} onClick={closeModal}>Report</button>
                </div>
            )}
        </>
    )
}

export default EditDeleteCommentModal
