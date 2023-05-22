import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getAllVideosThunk } from "../../store/videos";
import { getSingleUserThunk } from "../../store/users";
import OpenModalButton from "../OpenModalButton";
import DeleteVideoModal from "../DeleteVideoModal";


function ChannelPage() {

    const dispatch = useDispatch()
    let {channelId} = useParams()
    channelId = parseInt(channelId)
    console.log('channelId', channelId)
    console.log('typeof channelId', typeof channelId)

    const user = useSelector(state => state.users[channelId])
    const allVideos = useSelector(state => state.videos)

    useEffect(() => {
            dispatch(getAllVideosThunk())
            dispatch(getSingleUserThunk(channelId))
    }, [dispatch, channelId])


    if (!user) return null

    console.log('user', user)
    console.log('allVideos', allVideos)

    const channelVideos = Object.values(allVideos).filter(video => video.userId === channelId)
    console.log('channelVideos', channelVideos)

    const channelVideoList = channelVideos.map(video => (
        <>
        <NavLink key={video.id} to={`/videos/${video.id}`}>
            <div className="single-video">
                <img src={video.thumbnail}/>
            </div>
        </NavLink>
        </>
    ))

    return (
        <>
            <h1>Channel Page</h1>
            <div className="channel-videos-container">
                {channelVideoList}
            </div>
        </>
    )
}

export default ChannelPage
