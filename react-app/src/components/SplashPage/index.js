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

    const videoList = videosArr.map(video => (
        <div className="video">
            <NavLink key={video.id} to={`/videos/${video.id}`}>
                <img src={video.thumbnail}/>
                <h3>{video.name}</h3>
            </NavLink>
            <div className="video-details">
                {'Need to make a user page'}
                <NavLink key={video.user.id} to={`/channels/${video.user.id}`}>
                    <h5>{video.user.username}</h5>
                </NavLink>
            </div>
        </div>
    ))

    return (
        <>
            <div className="all-videos-container">
                {videoList}
            </div>


        </>
    )

}

export default SplashPage
