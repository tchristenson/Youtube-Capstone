import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import { getSingleUserThunk } from "../../store/users";
import styles from './ChannelPage.module.css'


function ChannelPage() {

    const dispatch = useDispatch()
    let {channelId} = useParams()
    const history = useHistory()
    channelId = parseInt(channelId)
    console.log('channelId', channelId)
    console.log('typeof channelId', typeof channelId)

    const user = useSelector(state => state.users[channelId])
    const allVideos = useSelector(state => state.videos)

    useEffect(() => {
            dispatch(getAllVideosThunk())
            dispatch(getSingleUserThunk(channelId))
    }, [dispatch, channelId])

    console.log('user', user)


    if (!user) return null

    console.log('user', user)
    console.log('allVideos', allVideos)

    const channelVideos = Object.values(allVideos).filter(video => video.userId === channelId)
    console.log('channelVideos', channelVideos)

    const channelVideoList = channelVideos.map(video => (
        <div key={video.id} className={styles["single-video"]}>
            <NavLink to={`/videos/${video.id}`}>
                <img src={video.thumbnail}/>
            </NavLink>
            <div className={styles["single-video-details"]}>
                <NavLink to={`/videos/${video.id}`}>
                    <h3>{video.name}</h3>
                </NavLink>
            </div>
        </div>
    ))

    return (
        <div className={styles['channel-page-container']}>
            <div className={styles['channel-information']}>
                <div className={styles['channel-picture-container']}>
                {user.profilePicture ? (
                        <img className={styles['channel-picture']} src={user.profilePicture}/>
                    ) : (
                        <h1 className={styles['channel-icon']}>{user.username[0]}</h1>
                    )}
                </div>

                <div className={styles['user-info-container']}>
                    <h3>{`${user.firstName} ${user.lastName}`}</h3>
                    <h5>{`@${user.username}`}</h5>
                    <h5>
                        {channelVideoList.length === 1 ? (
                        `${channelVideoList.length} video`
                        ) : (
                        `${channelVideoList.length} videos`
                        )}
                    </h5>
                    <h5 className={styles['user-about']}>{user.about}</h5>
                </div>

                <div className={styles['buttons-container']}>
                    <button>Subscribe</button>
                </div>
            </div>

            <div className={styles['channel-videos']}>
                {channelVideoList}
            </div>
        </div>
    )
}

export default ChannelPage
