import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { getSingleVideoThunk } from "../../store/videos";
import { getCommentsByVideoIdThunk } from "../../store/comments";
import NewComment from "../NewComment";
import CommentList from "../CommentList";
import styles from './SingleVideoPage.module.css'

function SingleVideoPage() {

    const dispatch = useDispatch()
    const {videoId} = useParams()

    useEffect(() => {
        dispatch(getSingleVideoThunk(videoId))
        dispatch(getCommentsByVideoIdThunk(videoId))
    }, [dispatch, videoId])

    const video = useSelector(state => state.videos[videoId])
    const comments = useSelector(state => state.comments)
    const sessionUser = useSelector(state => state.session.user)

    if (!video) return null

    const commentsArr = Object.values(comments)
    // console.log('commentsArr inside SingleVideoPage', commentsArr)
    // console.log('video inside SingleVideoPage', video)
    // console.log('comments inside SingleVideoPage', comments)

    return (
        <div className={styles['container']}>
            <div className={styles['main-video-column']}>
                <video controls >
                    <source src={video.content}/>
                </video>
                <h3>{video.name}</h3>
                <div className={styles['video-owner-details']}>
                    <NavLink key={video.user.id} to={`/channels/${video.user.id}`}>
                        <img className={styles['profile-picture']} src={video.user.profilePicture}/>
                        <h5>{video.user.username}</h5>
                    </NavLink>

                </div>
                <div className={styles['video-description']}>
                    <h6>{video.name}</h6>
                    <p>{video.description}</p>
                </div>
                <div className={styles['comment-input-container']}>
                    <img className={styles['session-user-profile-picture']} src={sessionUser?.profilePicture}/>
                    <div><NewComment video={video}/></div>

                </div>
                <div className="all-comments-container">
                    <CommentList video={video} commentsArr={commentsArr} sessionUser={sessionUser}/>
                </div>
            </div>
            <div className={styles['secondary-column']}>
                <h1>Other videos to go in this column</h1>

            </div>
        </div>
    )
}

export default SingleVideoPage
