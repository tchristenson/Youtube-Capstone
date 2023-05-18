
// ----------------------------------------  ACTIONS  ----------------------------------------

const UPLOAD_VIDEO = 'videos/UPLOAD_VIDEO'
const GET_SINGLE_VIDEO = 'videos/GET_SINGLE_VIDEO'
const GET_ALL_VIDEOS = 'videos/GET_ALL_VIDEOS'
const EDIT_VIDEO = 'videos/EDIT_VIDEO'
const DELETE_VIDEO = 'videos/DELETE_VIDEO'


const uploadVideoAction = video => {
    return {
        type: UPLOAD_VIDEO,
        video
    }
}

const getSingleVideoAction = video => {
    return {
        type: GET_SINGLE_VIDEO,
        video
    }
}

const getAllVideosAction = videos => {
    return {
        type: GET_ALL_VIDEOS,
        videos
    }
}

const editVideoAction = video => {
    return {
        type: EDIT_VIDEO,
        video
    }
}

const deleteVideoAction = videoId => {
    return {
        type: DELETE_VIDEO,
        videoId
    }
}


// ----------------------------------------  THUNKS  ----------------------------------------

export const uploadVideoThunk = video => async (dispatch) => {
    for (let key of video.entries()) {
        console.log('formData inside of the thunk', key[0] + '----->' + key[1]);
      }
    const response = await fetch('/api/videos/new', {
        method: 'POST',
        body: video
    })
    if (response.ok) {
        const video = await response.json()
        console.log('response.json() inside of thunk', video)
        dispatch(uploadVideoAction(video));
        return video
    }
}

export const getSingleVideoThunk = videoId => async (dispatch) => {
    const response = await fetch(`/api/videos/${videoId}`)
    if (response.ok) {
        const video = await response.json()
        dispatch(getSingleVideoAction(video))
        return video
    }
}

export const getAllVideosThunk = () => async (dispatch) => {
    const response = await fetch('/api/videos')
    if (response.ok) {
        const videos = await response.json()
        console.log('videos response from backend', videos)
        dispatch(getAllVideosAction(videos))
        return videos
    }
}

export const editVideoThunk = video => async (dispatch) => {
    const videoId = parseInt(video.get('id'))
    const response = await fetch(`/api/videos/${videoId}/edit`, {
        method: 'PUT',
        body: video
    })
    if (response.ok) {
        const video = await response.json()
        dispatch(editVideoAction(video))
        return video
    }
}

export const deleteVideoThunk = videoId => async (dispatch) => {
    const response = await fetch (`/api/videos/${videoId}/delete`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(deleteVideoAction(videoId))
        return {'message': 'delete successful'}
    }
}


// ----------------------------------------  REDUCER  ----------------------------------------

const videoReducer = (state = {}, action) => {
    let newState
    switch (action.type) {
        case UPLOAD_VIDEO:
            newState = {...state}
            newState[action.video.id] = action.video
            return newState
        case GET_SINGLE_VIDEO:
            newState = {...state}
            newState[action.video.id] = action.video
            return newState
        case GET_ALL_VIDEOS:
            newState = {...state}
            action.videos.Videos.forEach(video => newState[video.id] = video)
            return newState
        case EDIT_VIDEO:
            newState = {...state}
            newState[action.video.id] = action.video
            return newState
        case DELETE_VIDEO:
            newState = {...state}
            delete newState[action.videoId]
            return newState
        default:
            return state
    }
}

export default videoReducer
