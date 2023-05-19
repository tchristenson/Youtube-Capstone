import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addCommentThunk } from "../../store/comments";
import { useModal } from "../../context/Modal";



function EditCommentModal({comment}) {

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState(comment.content)
    const [hasSubmitted, setHasSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)

        const formData = new FormData()

        formData.append('content', content)

        for (let key of formData.entries()) {
            console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
          }

        await dispatch(addCommentThunk(formData))

        setContent('')
        setHasSubmitted(false)
    }

    return (
        <div className="comment-container">
            <form
                onSubmit={(e) => handleSubmit(e)}
            >
                <div>
                    <input
                        type="textarea"
                        onChange={(e) => setContent(e.target.value)}
                        value={content}
                        >
                    </input>
                </div>

                <button disabled={content? false : true} type="submit">Save</button>
                <button onClick={closeModal}>Cancel</button>
            </form>
        </div>
    )
}

export default EditCommentModal
