import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addCommentThunk } from "../../store/comments";



function NewComment({video}) {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)

        const formData = new FormData()

        formData.append('content', content)
        formData.append('video_id', video.id)

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
                        placeholder="Add a comment..."
                        >
                    </input>
                </div>

                <button disabled={content? false : true} type="submit">Comment</button>
                <button onClick={(e) => { e.preventDefault(); setContent(''); }} type="submit">Cancel</button>
            </form>
        </div>
    )
}

export default NewComment
