import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getSingleVideoThunk } from "../../store/videos";

function SingleVideoPage() {

    const dispatch = useDispatch()
    const {videoId} = useParams()

    useEffect(() => {
        dispatch(getSingleVideoThunk(videoId))
    }, [dispatch, videoId])

    const video = useSelector(state => state.videos[videoId])
    if (!video) return null

    console.log('video inside SingleVideoPage', video)











    return (
        <>
            <h1>Single Video Page</h1>

            <video controls width="800" height="600">
                <source src={video.content}/>
            </video>

        </>
    )
}

export default SingleVideoPage
