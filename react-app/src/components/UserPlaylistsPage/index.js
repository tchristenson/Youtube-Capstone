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
        <div key={video.id} className={styles['sidebar-video']}>
        <div className={styles['sidebar-thumbnail']}>
            <NavLink  to={`/videos/${video.id}`}>
                <img className={styles['playlist-video']} src={video.thumbnail} alt="Video Thumbnail"/>
            </NavLink>
        </div>
        <div className={styles['sidebar-video-details']}>
            <NavLink to={`/videos/${video.id}`}>
                <h5 className={styles['sidebar-video-name']}>{video.name}</h5>
            </NavLink>
        </div>
    </div>
    ))

    return (

        <div className={styles["playlist-page-container"]}>
            <div className={styles["playlist-thumbnail-container"]}>
                <img className={styles["playlist-thumbnail"]} src={playlist?.videos[0].thumbnail}/>
                <h3>{playlist?.name}</h3>
                <h5>{`${sessionUser.firstName} ${sessionUser.lastName}`}</h5>
                <h6>{`${playlist?.videos.length} videos`}</h6>
            </div>

            <div className={styles["playlist-videos-container"]}>
                {playlistVideos}
            </div>
        </div>
    )
}

export default UserPlaylistsPage
