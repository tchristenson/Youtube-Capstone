import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import DeleteVideoModal from "../DeleteVideoModal";
import EditVideoPage from "../EditVideoPage";
import styles from './EditDeleteVideoModal.module.css'




function EditDeleteVideoModal({video}) {
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    return (
        <div className={styles['buttons-container']}>
            <OpenModalButton buttonText='Edit' modalComponent={<EditVideoPage video={video}/>}></OpenModalButton>
            <OpenModalButton buttonText='Delete' modalComponent={<DeleteVideoModal video={video}/>}></OpenModalButton>
        </div>
    )
}

export default EditDeleteVideoModal
