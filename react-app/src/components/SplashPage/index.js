import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import styles from './SplashPage.module.css'

function SplashPage() {

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getAllVideosThunk())
    }, [dispatch])

    const videos = useSelector(state => state.videos)
    if (!videos) return null

    const videosArr = Object.values(videos)

    const videoList = videosArr.map(video => (
        <div className={styles.video}>
            <NavLink key={video.id} to={`/videos/${video.id}`}>
                <img className={styles.thumbnail} src={video.thumbnail}/>
            </NavLink>
            <div className={styles['video-info']}>
                <NavLink key={video.user.id} to={`/channels/${video.user.id}`}>
                    <img className={styles['profile-picture']} src={video.user.profilePicture}/>
                </NavLink>
                <NavLink key={video.id} to={`/videos/${video.id}`}>
                    <h3 className={styles.h3link}>{video.name}</h3>
                </NavLink>
            </div>
            <div>
                <NavLink key={video.user.id} to={`/channels/${video.user.id}`}>
                    <h5 className={styles.h5link}>{video.user.username}</h5>
                </NavLink>
            </div>
        </div>
    ))

    return (
        <>
            <div className={styles['all-videos-container']}>
                {videoList}
            </div>


        </>
    )

}

export default SplashPage
