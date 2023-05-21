
// ----------------------------------------  ACTIONS  ----------------------------------------

const ADD_COMMENT = 'comments/ADD_COMMENT'
const GET_COMMENTS_BY_VIDEO_ID = 'comments/GET_COMMENTS_BY_VIDEO_ID'
const DELETE_COMMENT = 'comments/DELETE_COMMENT'
const EDIT_COMMENT = 'comments/EDIT_COMMENT'


const addCommentAction = comment => {
    return {
        type: ADD_COMMENT,
        comment
    }
}

const getCommentsByVideoIdAction = comments => {
    return {
        type: GET_COMMENTS_BY_VIDEO_ID,
        comments
    }
}

const deleteCommentAction = commentId => {
    return {
        type: DELETE_COMMENT,
        commentId
    }
}

const editCommentAction = comment => {
    return {
        type: EDIT_COMMENT,
        comment
    }
}



// ----------------------------------------  THUNKS  ----------------------------------------

export const addCommentThunk = comment => async (dispatch) => {
    console.log('checking if I am inside the addCommentThunk')
    for (let key of comment.entries()) {
        console.log('formData inside thunk', key[0] + '----->' + key[1]);
      }
    const response = await fetch('/api/comments/new', {
        method: 'POST',
        body: comment
    })
    console.log('repsonse inside of thunk', response)
    if (response.ok) {
        const comment = await response.json()
        dispatch(addCommentAction(comment))
        return comment
    }
}

export const getCommentsByVideoIdThunk = videoId => async (dispatch) => {
    console.log('videoId inside getCommentsByVideoIdThunk', videoId)
    const response = await fetch(`/api/comments/${videoId}`)
    if (response.ok) {
        const comments = await response.json()
        console.log('response.json() inside getCommentsByVideoIdThunk', comments)
        dispatch(getCommentsByVideoIdAction(comments))
        return comments
    }
}

export const deleteCommentThunk = commentId => async (dispatch) => {
    const response = await fetch (`/api/comments/${commentId}/delete`, {
        method: 'DELETE'
    });
    if (response.ok) {
        dispatch(deleteCommentAction(commentId))
        return {'message': 'delete successful'}
    }
}

export const editCommentThunk = comment => async (dispatch) => {
    const commentId = parseInt(comment.get('id'))
    const response = await fetch(`/api/comments/${commentId}/edit`, {
        method: 'PUT',
        body: comment
    })
    if (response.ok) {
        const comment = await response.json()
        dispatch(editCommentAction(comment))
        return comment
    }
}



// ----------------------------------------  REDUCER  ----------------------------------------

const commentReducer = (state = {}, action) => {
    let newState
    switch(action.type) {
        case ADD_COMMENT:
            newState = {...state}
            newState[action.comment.id] = action.comment
            return newState
        case GET_COMMENTS_BY_VIDEO_ID:
            const updatedComments = action.comments.Comments.reduce((acc, comment) => {
                acc[comment.id] = comment;
                return acc;
              }, {});
            return {
            ...updatedComments
            };
        case DELETE_COMMENT:
            newState = {...state}
            delete newState[action.commentId]
            return newState
        case EDIT_COMMENT:
            newState = {...state}
            newState[action.comment.id] = action.comment
            return newState
        default:
            return state
    }
}

export default commentReducer
