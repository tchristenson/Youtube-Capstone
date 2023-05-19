import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getSingleVideoThunk } from "../../store/videos";
import { getCommentsByVideoIdThunk } from "../../store/comments";
import NewComment from "../NewComment";
import EditDeleteCommentModal from "../EditDeleteCommentModal";
import OpenModalIcon from "../OpenModalIcon";
import LoginFormModal from "../LoginFormModal";

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
    console.log('commentsArr inside SingleVideoPage', commentsArr)


    console.log('video inside SingleVideoPage', video)
    console.log('comments inside SingleVideoPage', comments)

    return (
        <>
            <h1>Single Video Page</h1>

            <video controls width="800" height="600">
                <source src={video.content}/>
            </video>
            <NewComment video={video}/>
            <div className="all-comments-container">
                <ul className="comment-container">
                    {commentsArr.map(comment => (
                        <div key={comment.id}>
                            <li>{comment.content}</li>
                                {sessionUser && (
                                <OpenModalIcon modalComponent={<EditDeleteCommentModal video={video} comment={comment}/>}></OpenModalIcon>
                            )}
                                {!sessionUser && (
                                <OpenModalIcon modalComponent={<LoginFormModal/>}></OpenModalIcon>
                            )}
                        </div>
                    ))}
                </ul>
            </div>
        </>
    )
}

export default SingleVideoPage
