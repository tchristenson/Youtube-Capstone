import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import { getSingleUserThunk } from "../../store/users";
import OpenModalButton from "../OpenModalButton";
import DeleteVideoModal from "../DeleteVideoModal";
import styles from './UserProfilePage.module.css'
import OpenModalIcon from "../OpenModalIcon";
import EditDeleteVideoModal from "../EditDeleteVideoModal";


function UserProfilePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {userId} = useParams()
    console.log('userId', userId)

    const sessionUser = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const allVideos = useSelector(state => state.videos)

    useEffect(() => {
        dispatch(getAllVideosThunk())
        dispatch(getSingleUserThunk(userId))
    }, [dispatch, userId])

    useEffect(() => {
        if (sessionUser && user && sessionUser.id !== user.id) {
            history.push('/')
        }
    }, [sessionUser, user, history])


    if (!sessionUser) return null
    if (!user) return null

    console.log('sessionUser', sessionUser)
    console.log('user', user)
    console.log('allVideos', allVideos)

    const userVideos = Object.values(allVideos).filter(video => video.userId === sessionUser.id)

    const userVideoList = userVideos.map(video => (

        <div key={video.id} className={styles["single-video"]}>
            <NavLink to={`/videos/${video.id}`}>
                <img src={video.thumbnail}/>
            </NavLink>
            <div className={styles["single-video-details"]}>
                <NavLink to={`/videos/${video.id}`}>
                    <h3>{video.name}</h3>
                </NavLink>
                <OpenModalIcon modalComponent={<EditDeleteVideoModal video={video}/>}></OpenModalIcon>
            </div>
        </div>

    ))

    return (


        <div className={styles['profile-page-container']}>
            <div className={styles['profile-information']}>
                <div className={styles['profile-picture-container']}>
                    <img className={styles['profile-picture']} src={sessionUser.profilePicture}/>

                </div>
                <div className={styles['user-info-container']}>
                    <h3>{`${sessionUser.firstName} ${sessionUser.lastName}`}</h3>
                    <h5>{`${sessionUser.username}`}</h5>
                    <h5>{`${userVideoList.length} videos`}</h5>
                </div>
            </div>

            <div className={styles['profile-videos']}>
                {userVideoList}
            </div>

            <div className={styles['profile-playlists']}>
                <h2>Placeholder for Playlists</h2>

            </div>

            <div className={styles['profile-subscriptions']}>
                <h2>Placeholder for Subscriptions</h2>

            </div>
        </div>

    )
}

export default UserProfilePage
