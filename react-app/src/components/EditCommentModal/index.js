import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { editCommentThunk } from "../../store/comments";
import { useModal } from "../../context/Modal";
import styles from './EditCommentModal.module.css'



function EditCommentModal({comment}) {

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState(comment.content)
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)
        if (validationErrors.length) return alert('Comment cannot exceed 10,000 characters')

        const formData = new FormData()

        formData.append('content', content)
        formData.append('id', comment.id)

        for (let key of formData.entries()) {
            console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
          }

        await dispatch(editCommentThunk(formData))

        setContent('')
        setHasSubmitted(false)
        setValidationErrors([])
        closeModal()
    }

    useEffect(() => {
        const errors = [];
        if (!content) errors.push('Comment cannot be empty')
        if (content.length > 10000) errors.push('Comment cannot exceed 10,000 characters')
        setValidationErrors(errors)
    }, [content])

    return (
        <div className={styles['comment-container']}>
            <h2 className={styles["header"]}>Edit your comment</h2>
            <form
                onSubmit={(e) => handleSubmit(e)}
            >
                <div className={styles["input"]}>
                    <textarea
                        onChange={(e) => setContent(e.target.value)}
                        value={content}
                        >
                    </textarea>
                </div>

                <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={(e) => {
                    e.preventDefault(); setContent(''); closeModal() }}
                    type="submit">Cancel</button>
                <button
                    className={content ? styles['submit-button-active'] : styles['submit-button']}
                    disabled={content ? false : true}
                    type="submit">Save</button>

            </div>
            </form>
        </div>
    )
}

export default EditCommentModal
