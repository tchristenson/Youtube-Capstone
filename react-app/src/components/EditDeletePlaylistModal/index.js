import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import styles from './EditDeletePlaylistModal.module.css'
import EditPlaylistModal from "../EditPlaylistModal";
import DeletePlaylistModal from "../DeletePlaylistModal";



function EditDeletePlaylistModal({playlist}) {
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    return (
        <>
            {sessionUser && sessionUser.id === playlist.userId && (

                <div className={styles['buttons-container']}>

                    <OpenModalButton buttonText='Edit' modalComponent={<EditPlaylistModal playlist={playlist}/>}></OpenModalButton>
                    <OpenModalButton buttonText='Delete' modalComponent={<DeletePlaylistModal playlist={playlist}/>}></OpenModalButton>

                </div>

            )}
        </>
    )
}

export default EditDeletePlaylistModal
