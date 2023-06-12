
// ----------------------------------------  ACTIONS  ----------------------------------------

const CREATE_PLAYLIST = 'playlists/CREATE_PLAYLIST'
const GET_SINGLE_PLAYLIST = 'playlists/GET_SINGLE_PLAYLIST'
const ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST = 'playlists/ADD_OR_REMOVE_VIDEO_FROM_PLAYLIST'
const EDIT_PLAYLIST = 'playists/EDIT_PLAYLIST'
const DELETE_PLAYLIST = 'playlists/DELETE_PLAYLIST'

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

const editPlaylistAction = playlist => {
    return {
        type: EDIT_PLAYLIST,
        playlist
    }
}

const deletePlaylistAction = playlistId => {
    return {
        type: DELETE_PLAYLIST,
        playlistId
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
        console.log('playlist result from thunk', playlist)
        dispatch(addOrRemoveVideoFromPlaylistAction(playlist))
        return playlist
    }
}

export const editPlaylistThunk = playlist => async (dispatch) => {
    for (let key of playlist.entries()) {
        console.log('formData inside thunk', key[0] + '----->' + key[1]);
      }
    const playlistId = parseInt(playlist.get('id'))
    const response = await fetch(`/api/playlists/${playlistId}/edit`, {
        method: 'PUT',
        body: playlist
    })
    if (response.ok) {
        const playlist = await response.json()
        dispatch(editPlaylistAction(playlist))
        return playlist
    }
}

export const deletePlaylistThunk = playlistId => async (dispatch) => {
    const response = await fetch(`/api/playlists/${playlistId}/delete`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(deletePlaylistAction(playlistId))
        return {'message': 'delete successful'}
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
        case EDIT_PLAYLIST:
            newState = {...state}
            newState[action.playlist.id] = action.playlist
            return newState
        case DELETE_PLAYLIST:
            newState = {...state}
            delete newState[action.playlistId]
            return newState
        default:
            return state
    }
}

export default playlistReducer
