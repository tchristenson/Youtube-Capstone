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
        <div key={video.id} className={styles.video}>
            <NavLink  to={`/videos/${video.id}`}>
                <img className={styles.thumbnail} src={video.thumbnail}/>
            </NavLink>
            <div className={styles['video-info']}>
                <NavLink to={`/channels/${video.user.id}`}>
                    { video.user.profilePicture ? (
                        <img className={styles['profile-picture']} src={video.user.profilePicture}/>
                    ) : (
                        <h3 className={styles['profile-icon']}>{video.user.username[0]}</h3>
                    )}
                </NavLink>
                <NavLink to={`/videos/${video.id}`}>
                    <h3 className={styles.h3link}>{video.name}</h3>
                </NavLink>
            </div>
            <div>
                <NavLink to={`/channels/${video.user.id}`}>
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
