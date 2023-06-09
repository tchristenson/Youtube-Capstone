import { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, NavLink, useHistory } from "react-router-dom";
import { getSinglePlaylistThunk } from "../../store/playlists";
import styles from './UserPlaylistsPage.module.css'
import OpenModalIcon from "../OpenModalIcon";

function UserPlaylistsPage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const {userId, playlistId} = useParams()

    const [playlist, setPlaylist] = useState(null)
    // console.log('userId', userId)
    // console.log('playlistId', playlistId)

    useEffect(() => {
        dispatch(getSinglePlaylistThunk(playlistId)).then(data => setPlaylist(data))
    }, [dispatch, playlistId])

    const sessionUser = useSelector(state => state.session.user)
    const user = useSelector(state => state.users[userId])
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
                <h3 className={styles["playlist-name"]}>{playlist?.name}</h3>
                <h5 className={styles["first-last-name"]}>{`${sessionUser.firstName} ${sessionUser.lastName}`}</h5>
                <h6 className={styles["playlist-video-count"]}>
                    {playlist?.videos.length === 1 ? (
                        `${playlist.videos.length} video`
                    ) : (
                        `${playlist.videos.length} videos`
                    )}
                </h6>
            </div>

            <div className={styles["playlist-videos-container"]}>
                {playlistVideos}
            </div>
        </div>
    )
}

export default UserPlaylistsPage
