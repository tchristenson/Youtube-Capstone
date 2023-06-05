import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink } from "react-router-dom";
import { likeVideoThunk } from "../../store/videos";
import { getCommentsByVideoIdThunk } from "../../store/comments";
import { getAllVideosThunk } from "../../store/videos";
import { subscribeUnsubscribeThunk } from "../../store/session";
import { getSingleVideoThunk } from "../../store/videos";
import UnsubscribeModal from "../UnsubscribeModal"
import OpenModalButton from "../OpenModalButton";
import NewComment from "../NewComment";
import CommentList from "../CommentList";
import styles from './SingleVideoPage.module.css'
import LoginFormModal from "../LoginFormModal";
import OpenModalIcon from "../OpenModalIcon";
import NewPlaylistModal from "../NewPlaylistModal";

function SingleVideoPage() {

    const dispatch = useDispatch()
    const {videoId} = useParams()
    // const [video, setVideo] = useState(null)

    useEffect(() => {
        window.scrollTo(0, 0)
      }, [videoId])

    useEffect(() => {
        // dispatch(getSingleVideoThunk(videoId)).then(data => setVideo(data))
        dispatch(getAllVideosThunk())
        dispatch(getCommentsByVideoIdThunk(videoId))
    }, [dispatch, videoId])

    const handleLike = (e) => {
        e.preventDefault()
        if (sessionUser) {
            dispatch(likeVideoThunk(videoId, sessionUser.id))
        }
    }

    const handleSubscribe = (e) => {
        e.preventDefault()
        dispatch(subscribeUnsubscribeThunk(video.user.id, sessionUser.id))
    }

    // console.log('video ------>', video)

    const video = useSelector(state => state.videos[videoId])
    const comments = useSelector(state => state.comments)
    const allVideos = useSelector(state => state.videos)
    const sessionUser = useSelector(state => state.session.user)

    if (!video) return null

    const commentsArr = Object.values(comments)
    const allVideosArr = Object.values(allVideos)
    const filteredVideos = allVideosArr.filter(currVideo => currVideo.id !== video.id)
    const userLike = video.userLikes.filter(like => like.id === sessionUser?.id)
    console.log('userLike', userLike)
    // console.log('filteredVideos', filteredVideos)
    // console.log('commentsArr inside SingleVideoPage', commentsArr)
    console.log('video inside SingleVideoPage', video)
    console.log('sessionUser inside Single Video Page', sessionUser)
    // console.log('comments inside SingleVideoPage', comments)

    const sidebarVideos = filteredVideos.map(video => (
        <div key={video.id} className={styles['sidebar-video']}>
            <div className={styles['sidebar-thumbnail']}>
                <NavLink  to={`/videos/${video.id}`}>
                    <img src={video.thumbnail} alt="Video Thumbnail"/>
                </NavLink>
            </div>
            <div className={styles['sidebar-video-details']}>
                <NavLink to={`/videos/${video.id}`}>
                    <h5 className={styles['sidebar-video-name']}>{video.name}</h5>
                </NavLink>
                <NavLink to={`/channels/${video.user?.id}`}>
                    <h5 className={styles['h5link']}>{video.user?.username}</h5>
                </NavLink>
            </div>

        </div>
    ))

    return (
        <div className={styles['container']}>
            <div key={video.id} className={styles['main-video-column']}>
                <div className={styles['main-video-container']}>
                    <video controls className={styles['main-video']}>
                        <source src={video.content}/>
                    </video>
                </div>
                <div className={styles['name-like-playlist-container']}>
                    <div>
                        <h3 className={styles['main-video-name']}>{video.name}</h3>
                    </div>
                    <div className={styles['like-playlist-buttons-container']}>
                        <div className={styles['like-info-container']} onClick={handleLike}>
                            <button className={styles['like-button']}>
                                {sessionUser && userLike.length === 1 &&
                                    <i id={styles['user-has-liked']} className="fa-solid fa-thumbs-up"></i>
                                }
                                {sessionUser && userLike.length === 0 &&
                                    <i id={styles['user-has-not-liked']} className="fa-solid fa-thumbs-up"></i>
                                }
                                {!sessionUser &&
                                <OpenModalIcon className="fa-solid fa-thumbs-up" modalComponent={<LoginFormModal/>}></OpenModalIcon>
                                }
                            </button>
                            <h5 className={styles['like-count']}>{video.userLikes.length}</h5>
                        </div>
                        <div className={styles['playlist-info-container']}>
                            <OpenModalIcon modalComponent={<NewPlaylistModal video={video}/>} className="fa-solid fa-list"></OpenModalIcon>
                            <OpenModalIcon modalComponent={<NewPlaylistModal video={video}/>} className="fa-solid fa-plus"></OpenModalIcon>
                        </div>
                    </div>
                </div>
                <div className={styles['video-owner-details']}>
                    <NavLink to={`/channels/${video.user.id}`}>
                        { video.user.profilePicture ? (
                            <img className={styles['profile-picture']} src={video.user.profilePicture}/>
                        ) : (
                            <h3 className={styles['profile-icon']}>{video.user.username[0]}</h3>
                        )}
                        <h4>{video.user.username}</h4>
                    </NavLink>
                    <div className={styles["subscribe-buttons"]}>
                        {sessionUser && !sessionUser.subscribedIds.includes(video.user.id) &&
                            <button onClick={handleSubscribe} id={styles['subscribe-button']}>Subscribe</button>
                        }
                        {sessionUser && sessionUser.subscribedIds.includes(video.user.id) &&
                            <OpenModalButton className={styles.subscribedButton} buttonText='Subscribed' modalComponent={<UnsubscribeModal user={video.user} sessionUser={sessionUser}/>}></OpenModalButton>
                        }
                        {!sessionUser &&
                            <OpenModalButton className={styles.subscribeButtonInactive} buttonText='Subscribe' modalComponent={<LoginFormModal/>}></OpenModalButton>
                        }
                    </div>

                </div>
                <div className={styles['video-description']}>
                    {/* <h6>{video.name}</h6> */}
                    <h5>{video.description}</h5>
                </div>
                <div className={styles['comment-count']}>
                    {commentsArr.length === 1 ? (
                        <h4>{`${commentsArr.length} comment`}</h4>
                    ) : (
                        <h4>{`${commentsArr.length} comments`}</h4>

                    )}
                </div>
                <div className={styles['comment-input-container']}>
                    {!sessionUser && <i className="fa-solid fa-user"></i>}
                    {sessionUser && sessionUser.profilePicture &&
                        <img className={styles['session-user-profile-picture']} src={sessionUser?.profilePicture}/>}
                    {sessionUser && !sessionUser.profilePicture &&
                        <h3 className={styles['profile-icon']}>{sessionUser?.username[0]}</h3>}

                    <div><NewComment video={video}/></div>

                </div>
                <div className="all-comments-container">
                    <CommentList video={video} commentsArr={commentsArr} sessionUser={sessionUser}/>
                </div>
            </div>
            <div className={styles['sidebar']}>
                {sidebarVideos}
            </div>
        </div>
    )
}

export default SingleVideoPage
