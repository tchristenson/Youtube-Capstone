
// ----------------------------------------  ACTIONS  ----------------------------------------

const ADD_COMMENT = 'videos/ADD_COMMENT'


const addCommentAction = comment => {
    return {
        type: ADD_COMMENT,
        comment
    }
}



// ----------------------------------------  THUNKS  ----------------------------------------

export const addCommentThunk = comment => async (dispatch) => {
    // Need to make backend route
}
