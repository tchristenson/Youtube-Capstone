import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";



function NewComment() {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)

    const [content, setContent] = useState('')
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        setHasSubmitted(true)
        if (validationErrors.length) return alert('Your Post has errors, cannot submit!')

        const payload = {
            content
        }

        // dispatch create comment thunk





        setContent('')
        setValidationErrors([])
        setHasSubmitted(false)

    }




}
