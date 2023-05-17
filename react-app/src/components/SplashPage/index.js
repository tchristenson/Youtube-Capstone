import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";

function SplashPage() {

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllVideosThunk())
    }, [dispatch])

    const videos = useSelector(state => state.videos)
    if (!videos) return null

    const videosArr = Object.values(videos)
    // console.log('videosArr', videosArr)
    // console.log('videos', videos)

    const videoList = videosArr.map(video => (
        <NavLink key={video.id} to={`/videos/${video.id}`}>
            <div className="single-video">
                <img src={video.thumbnail}/>
            </div>
        </NavLink>
    ))

    return (
        <>
            <h1>Splash Page</h1>
            <div className="all-videos-container">
                {videoList}
            </div>


        </>
    )

}

export default SplashPage
