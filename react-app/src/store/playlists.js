
// ----------------------------------------  ACTIONS  ----------------------------------------

const CREATE_PLAYLIST = 'playlists/CREATE_PLAYLIST'

const createPlaylistAction = playlist => {
    return {
        type: CREATE_PLAYLIST,
        playlist
    }
}


// ----------------------------------------  THUNKS  ----------------------------------------

export const createPlaylistThunk = playlist => async (dispatch) => {

}
