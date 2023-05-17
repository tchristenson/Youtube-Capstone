
// ----------------------------------------  ACTIONS  ----------------------------------------

const UPLOAD_VIDEO = 'videos/UPLOAD_VIDEO'
const GET_SINGLE_VIDEO = 'videos/GET_SINGLE_VIDEO'
const GET_ALL_VIDEOS = 'videos/GET_ALL_VIDEOS'


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
        default:
            return state
    }
}

export default videoReducer
