import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addCommentThunk } from "../../store/comments";



function NewComment({video}) {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState('')
    // const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)
        // if (validationErrors.length) return alert('Your Post has errors, cannot submit!')

        const formData = new FormData()

        formData.append('content', content)
        formData.append('video_id', video.id)

        for (let key of formData.entries()) {
            console.log('formData before dispatching thunk', key[0] + '----->' + key[1]);
          }


        // dispatch create comment thunk
        await dispatch(addCommentThunk(formData))

        setContent('')
        // setValidationErrors([])
        setHasSubmitted(false)
    }

    // useEffect(() => {
    //     const errors = [];
    //     if (!content) errors.push('Text required')
    //     setValidationErrors(errors)
    // }, [content])

    return (
        <div className="comment-container">
            <h2 className="form-header">Add a comment</h2>

            <form
                onSubmit={(e) => handleSubmit(e)}
                // encType="multipart/form-data"
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
