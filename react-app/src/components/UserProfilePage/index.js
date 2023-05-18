import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import { getSingleUserThunk } from "../../store/users";
import OpenModalButton from "../OpenModalButton";
import DeleteVideoModal from "../../DeleteVideoModal";


function UserProfilePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {userId} = useParams()

    const sessionUser = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const allVideos = useSelector(state => state.videos)

    useEffect(() => { // do i need this?
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
        <>
        <NavLink key={video.id} to={`/videos/${video.id}`}>
            <div className="single-video">
                <img src={video.thumbnail}/>
            </div>
        </NavLink>
        <OpenModalButton buttonText='Delete Video' modalComponent={<DeleteVideoModal videoId = {video.id}/>}></OpenModalButton>
        </>
    ))

    return (
        <>
            <h1>User Profile Page</h1>
            <div className="user-videos-container">
                {userVideoList}
            </div>
        </>
    )
}

export default UserProfilePage
