import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import { getSingleUserThunk, getAllUsersThunk } from "../../store/users";
import UnsubscribeModal from "../UnsubscribeModal"
import OpenModalButton from "../OpenModalButton";
import styles from './UserProfilePage.module.css'
import OpenModalIcon from "../OpenModalIcon";
import EditDeleteVideoModal from "../EditDeleteVideoModal";
import NewVideoPage from "../NewVideoPage";
import UserPlaylistsPage from "../UserPlaylistsPage";


function UserProfilePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {userId} = useParams()
    // console.log('userId', userId)

    const sessionUser = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const allVideos = useSelector(state => state.videos)
    const allUsers = useSelector(state => state.users)

    useEffect(() => {
        dispatch(getAllVideosThunk())
        dispatch(getSingleUserThunk(userId))
        dispatch(getAllUsersThunk())
    }, [dispatch, userId])

    useEffect(() => {
        if (sessionUser && user && sessionUser.id !== user.id) {
            history.push('/')
        }
    }, [sessionUser, user, history])



    if (!sessionUser) return null
    if (!user) return null

    console.log('sessionUser ------->', sessionUser)
    console.log('allUsers ------->', allUsers)
    console.log('user ------>', user)
    // console.log('allVideos', allVideos)

    const allVideosArr = Object.values(allVideos)
    console.log('allVideosArr ------>', allVideosArr)
    const sessionUserVideos = Object.values(allVideos).filter(video => video.userId === sessionUser.id)
    const sessionUserSubscribed = Object.values(allUsers).filter(user => sessionUser.subscribedIds.includes(user.id))
    console.log('sessionUserSubscribed ------->', sessionUserSubscribed)

    const sessionUserVideoList = sessionUserVideos.map(video => (
        <div key={video.id} className={styles["single-video"]}>
            <NavLink to={`/videos/${video.id}`}>
                <img src={video.thumbnail}/>
            </NavLink>
            <div className={styles["single-video-details"]}>
                <NavLink to={`/videos/${video.id}`}>
                    <h5>{video.name}</h5>
                </NavLink>
                <OpenModalIcon className="fa-solid fa-ellipsis-vertical" modalComponent={<EditDeleteVideoModal video={video}/>}></OpenModalIcon>
            </div>
        </div>
    ))

    const sessionUserPlaylists = user.playlists.map(playlist => (
        <NavLink key={playlist.id} to={`/users/${user.id}/playlists/${playlist.id}`}>
        <div className={styles["single-video"]}>
            <img src={playlist.videos[0]?.thumbnail}/>
            <div className={styles["single-video-details"]}>
                    <h5>{playlist.name}</h5>
            </div>
        </div>
        </NavLink>
    ))

    console.log('sessionUserPlaylists', sessionUserPlaylists)

    const sessionUserSubscribedList = sessionUserSubscribed.map(user => (
        <div key={user.id} className={styles["single-subscribed"]}>
            <NavLink to={`/channels/${user.id}`}>
                <img src={user.profilePicture} className={styles["subscribed-profile-picture"]}/>
                <h5 className={styles["subscribed-username"]}>{user.username}</h5>
                <h5 className={styles["subscribed-count"]}>
                    {user.subscribersIds.length === 1 ? (
                        `${user.subscribersIds.length} subscriber`
                        ) : (
                        `${user.subscribersIds.length} subscribers`
                        )}
                </h5>
            </NavLink>
            <div id={styles["subscribed-button"]}>
                <OpenModalButton buttonText='Subscribed' modalComponent={<UnsubscribeModal user={user} sessionUser={sessionUser}/>}></OpenModalButton>
            </div>
        </div>
    ))

    return (


        <div className={styles['profile-page-container']}>
            <div className={styles['profile-information']}>
                <div className={styles['profile-picture-container']}>
                    {sessionUser.profilePicture ? (
                        <img className={styles['profile-picture']} src={sessionUser.profilePicture}/>
                    ) : (
                        <h1 className={styles['profile-icon']}>{sessionUser.username[0]}</h1>
                    )}
                </div>

                <div className={styles['user-info-container']}>
                    <h3>{`${sessionUser.firstName} ${sessionUser.lastName}`}</h3>
                    <h5>{`@${sessionUser.username}`}</h5>
                    <h5>
                        {sessionUserVideoList.length === 1 ? (
                        `${sessionUserVideoList.length} video`
                        ) : (
                        `${sessionUserVideoList.length} videos`
                        )}
                    </h5>
                </div>

                <div className={styles['buttons-container']}>
                    <OpenModalButton buttonText='Upload Video' modalComponent={<NewVideoPage/>}></OpenModalButton>
                </div>
            </div>

            <div className={styles['section']}>
                <h3 className={styles['section-header']}>Uploads</h3>
                <div className={styles['profile-videos']}>
                    {sessionUserVideoList}
                </div>
            </div>

            <div className={styles['section']}>
                <h3 className={styles['section-header']}>Playlists</h3>
                <div className={styles['playlist-videos']}>
                    {sessionUserPlaylists}
                </div>
            </div>

            <div className={styles['section']}>
                <h3 className={styles['section-header']}>Subscriptions</h3>
                <div className={styles['subscribed-to-users']}>
                    {sessionUserSubscribedList}
                </div>
            </div>

        </div>

    )
}

export default UserProfilePage
