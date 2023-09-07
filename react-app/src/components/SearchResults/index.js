import { useSelector } from "react-redux"
import styles from './SearchResults.module.css'
import { NavLink } from "react-router-dom"

function SearchResults() {

    const searchResults = useSelector(state => state.search)
    const searchResultsArr = Object.values(searchResults)
    console.log('searchResults', searchResults)
    console.log('searchResultsArr', searchResultsArr)

    const videosList = searchResultsArr.map(video => (
        <div key={video.id} className={styles['search-video']}>
            <div className={styles['thumbnail']}>
                <NavLink to={`/videos/${video.id}`}>
                    <img src={video.thumbnail} alt="Video Thumbnail"/>
                </NavLink>
            </div>
            <div className={styles['search-video-details']}>
                <NavLink to={`/videos/${video.id}`}>
                    <h5 className={styles['search-video-name']}>{video.name}</h5>
                </NavLink>
                <NavLink to={`/channels/${video.user?.id}`}>
                    <h5 className={styles['h5link']}>{video.user?.username}</h5>
                </NavLink>
            </div>
        </div>
    ))

    return (
        <div className={styles["search-results-container"]}>
            <h2 className={styles["header"]}>Your search results:</h2>
            <div>{videosList.length ? (
                videosList
            ) : (
                <h4>Nothing matched your search</h4>
            )}
            </div>
        </div>
    )
}

export default SearchResults
