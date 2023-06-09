
// ----------------------------------------  ACTIONS  ----------------------------------------

const CREATE_PLAYLIST = 'playlists/CREATE_PLAYLIST'
const GET_SINGLE_PLAYLIST = 'playlists/GET_SINGLE_PLAYLIST'
const ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST = 'playlists/ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST'

const createPlaylistAction = playlist => {
    return {
        type: CREATE_PLAYLIST,
        playlist
    }
}

const getSinglePlaylistAction = playlist => {
    return {
        type: GET_SINGLE_PLAYLIST,
        playlist
    }
}

const addOrRemoveVideoFromPlaylistAction = playlist => {
    return {
        type: ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST,
        playlist
    }
}


// ----------------------------------------  THUNKS  ----------------------------------------

export const createPlaylistThunk = (playlist) => async (dispatch) => {
//     for (let key of playlist.entries()) {
//     console.log('formData inside of the thunk', key[0] + '----->' + key[1]);
//   }
    const videoId = parseInt(playlist.get('id'))
    console.log('videoId', videoId)
    const response = await fetch(`/api/videos/${videoId}/playlists/new`, {
        method: 'POST',
        body: playlist
    });
    if (response.ok) {
        const playlist = await response.json()
        dispatch(createPlaylistAction(playlist))
        return playlist
    }
}

export const getSinglePlaylistThunk = playlistId => async (dispatch) => {
    const response = await fetch(`/api/playlists/${playlistId}`)
    if (response.ok) {
        const playlist = await response.json()
        dispatch(getSinglePlaylistAction(playlist))
        return playlist
    }
}

export const addOrRemoveVideoFromPlaylistThunk = (videoId, playlistId) => async (dispatch) => {
    const response = await fetch(`/api/videos/${videoId}/playlists/${playlistId}`, {
        method: 'POST',
        body: videoId, playlistId
    });
    if (response.ok) {
        const playlist = await response.json()
        dispatch(addOrRemoveVideoFromPlaylistAction(playlist))
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
        case GET_SINGLE_PLAYLIST:
            newState = {...state}
            newState[action.playlist.id] = action.playlist
            return newState
        case ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST:
            newState = {...state}
            newState[action.playlist.id] = action.playlist
            return newState
        default:
            return state
    }
}

export default playlistReducer
