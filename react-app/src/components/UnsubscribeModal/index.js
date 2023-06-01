import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { subscribeUnsubscribeThunk } from "../../store/session";
import styles from './UnsubscribeModal.module.css'

function UnsubscribeModal({user, sessionUser}) {
    const dispatch = useDispatch();

    const { closeModal } = useModal();


    const handleSubscribe = async (e) => {
        e.preventDefault()
        await dispatch(subscribeUnsubscribeThunk(user.id, sessionUser.id))
        closeModal()
    }

    return (
        <div className={styles['unsubscribe-modal']}>
            <h4 className={styles["header"]}>{`Unsubscribe from ${user.username}?`}</h4>
            <form onSubmit={handleSubscribe}>
            <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={closeModal}>Cancel</button>
                <button className={styles['submit-button-active']} type="submit">Unsubscribe</button>
            </div>
            </form>
        </div>
    )

}

export default UnsubscribeModal
