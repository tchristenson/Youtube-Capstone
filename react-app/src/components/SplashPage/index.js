import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import styles from './SplashPage.module.css'

function SplashPage() {

    const dispatch = useDispatch()
    const [query, setQuery] = useState('')

    useEffect(() => {
        dispatch(getAllVideosThunk())
    }, [dispatch])

    const videos = useSelector(state => state.videos)
    if (!videos) return null

    const videosArr = Object.values(videos)

    const videoList = videosArr.filter(video => {
        if (query === '') {
            return video;
        } else if (video.name.toLowerCase().includes(query.toLowerCase())) {
            return video
        } else if (video.user.username.toLowerCase().includes(query.toLowerCase())) {
            return video
        }
        })
        .map(video => (
        <div key={video.id} className={styles['video']}>
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
                <div className={styles['video-name-username']}>
                    <NavLink to={`/videos/${video.id}`}>
                        <h5 className={styles['video-name']}>{video.name}</h5>
                    </NavLink>
                    <NavLink to={`/channels/${video.user.id}`}>
                        <h5 className={styles.h5link}>{video.user.username}</h5>
                    </NavLink>
                </div>
            </div>
        </div>
    ))

    return (
        <div className={styles['splash-page-container']}>
            <div className={styles['search-bar-container']}>
                <input
                    className={styles['search-bar']}
                    value={query}
                    onChange={e => setQuery(e.target.value)}
                    type='search'
                    placeholder="Search"
                />
            </div>
            <div className={styles['all-videos-container']}>
                {videoList}
            </div>


        </div>
    )

}

export default SplashPage
