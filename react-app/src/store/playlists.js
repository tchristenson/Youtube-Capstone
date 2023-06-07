
// ----------------------------------------  ACTIONS  ----------------------------------------

const CREATE_PLAYLIST = 'playlists/CREATE_PLAYLIST'

const createPlaylistAction = playlist => {
    return {
        type: CREATE_PLAYLIST,
        playlist
    }
}


// ----------------------------------------  THUNKS  ----------------------------------------

export const createPlaylistThunk = videoId => async (dispatch) => {
    const response = await fetch(`/api/playlists/new`, {
        method: 'POST',
        body: videoId
    });
    if (response.ok) {
        const playlist = await response.json()
        dispatch(createPlaylistAction(playlist))
        return playlist
    }
}


// ----------------------------------------  REDUCER  ----------------------------------------

const playlistReducer = (state = {}, action) => {
    let newState
    switch(action.type) {
        case CREATE_PLAYLIST:
            newState = {...state}
            newState[action.playlist.id] = action.playlist
            return newState
        default:
                return state
    }
}

export default playlistReducer
