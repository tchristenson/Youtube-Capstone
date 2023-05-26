import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addCommentThunk } from "../../store/comments";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import { useModal } from "../../context/Modal";
import styles from './NewComment.module.css'



function NewComment({video}) {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)

        const formData = new FormData()
        if (validationErrors.length) return alert('Comment cannot exceed 10,000 characters')

        formData.append('content', content)
        formData.append('video_id', video.id)

        for (let key of formData.entries()) {
            console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
          }

        await dispatch(addCommentThunk(formData))

        setContent('')
        setHasSubmitted(false)
        setValidationErrors([])
    }

    useEffect(() => {
        const errors = [];
        if (!content.trim()) errors.push('Comment cannot be empty')
        if (content.length > 10000) errors.push('Comment cannot exceed 10,000 characters')
        setValidationErrors(errors)
    }, [content])

    return (
        <div className={styles['comment-container']}>
            <form
                onSubmit={(e) => handleSubmit(e)}
            >
                <div>
                    <input
                        className={styles['comment-input-box']}
                        type="textarea"
                        onChange={(e) => setContent(e.target.value)}
                        value={content}
                        placeholder="Add a comment..."
                        >
                    </input>
                </div>

                <div className={styles['buttons']}>
                    <button className={styles['cancel-button']} onClick={(e) => { e.preventDefault(); setContent(''); }} type="submit">Cancel</button>

                    {sessionUser && <button className={content.trim() ? styles['submit-button-active'] : styles['submit-button']} disabled={content.trim() ? false : true} type="submit">Comment</button>}
                    {!sessionUser &&
                        <OpenModalButton
                            buttonText="Comment"
                            modalComponent={<LoginFormModal />}
                        />}
                </div>
            </form>
        </div>
    )
}

export default NewComment
