import { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getSinglePlaylistThunk } from "../../store/playlists";
import styles from './UserPlaylistsPage.module.css'
import OpenModalIcon from "../OpenModalIcon";
import EditDeletePlaylistModal from "../EditDeletePlaylistModal";

function UserPlaylistsPage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {userId, playlistId} = useParams()

    useEffect(() => {
        dispatch(getSinglePlaylistThunk(playlistId))
    }, [dispatch, playlistId])

    const sessionUser = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
    const playlist = useSelector(state => state.playlists[playlistId])
    console.log('playlist', playlist)

    useEffect(() => {
        if (sessionUser && user && sessionUser.id !== user.id) {
            history.push('/')
        }
    }, [sessionUser, user, history])

    if (!playlist) return null

    const playlistVideos = playlist?.videos.map(video => (
        <NavLink key={video.id} to={`/videos/${video.id}`}>
            <div className={styles['sidebar-video']}>
                <div className={styles['sidebar-thumbnail']}>
                    <img className={styles['playlist-video']} src={video.thumbnail} alt="Video Thumbnail"/>
                </div>
                <div className={styles['sidebar-video-details']}>
                        <h5 className={styles['sidebar-video-name']}>{video.name}</h5>
                </div>
            </div>
        </NavLink>
    ))

    return (
        <div className={styles["playlist-page-container"]}>
            <div className={styles["playlist-thumbnail-container"]}>
                <img className={styles["playlist-thumbnail"]} src={playlist?.videos[0].thumbnail}/>
                <div className={styles["name-icon-container"]}>
                    <h3 className={styles["playlist-name"]}>{playlist?.name}</h3>
                    <OpenModalIcon className="fa-solid fa-ellipsis-vertical" modalComponent={<EditDeletePlaylistModal playlist={playlist}/>}></OpenModalIcon>
                </div>
                <h5 className={styles["first-last-name"]}>{`${sessionUser.firstName} ${sessionUser.lastName}`}</h5>
                <h5 className={styles["playlist-video-count"]}>
                    {playlist?.videos.length === 1 ? (
                        `${playlist.videos.length} video`
                    ) : (
                        `${playlist.videos.length} videos`
                    )}
                </h5>
            </div>

            <div className={styles["playlist-videos-container"]}>
                {playlistVideos}
            </div>
        </div>
    )
}

export default UserPlaylistsPage
