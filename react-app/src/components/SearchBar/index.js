import { useDispatch } from "react-redux"
import { useState } from "react"
import styles from './SearchBar.module.css'
import { searchVideosUsersThunk, clearSearchResultsThunk } from "../../store/search";
import { useHistory } from "react-router-dom";

function SearchBar() {

    const dispatch = useDispatch()
    const history = useHistory()
    const [query, setQuery] = useState('')

    const handleSearch = async (e) => {
        e.preventDefault()
        await dispatch(clearSearchResultsThunk())
        await dispatch(searchVideosUsersThunk(query))
        setQuery('')
        history.push('/search')
    }

    return (
            <div className={styles['search-bar-container']}>
                <input
                    className={styles['search-bar']}
                    value={query}
                    onChange={e => setQuery(e.target.value)}
                    type='search'
                    placeholder="Search"
                />
                <div onClick={handleSearch} className={styles['search-button-container']}>
                    <div className={styles['search-button']}>Search</div>
                    <i id='search-icon' className="fa-solid fa-magnifying-glass"></i>
                </div>
            </div>

    )
}

export default SearchBar
