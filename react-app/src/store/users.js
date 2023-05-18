
// ----------------------------------------  ACTIONS  ----------------------------------------
const GET_SINGLE_USER = 'users/GET_SINGLE_USER'


const getSingleUserAction = (user) => {
    return {
        type: GET_SINGLE_USER,
        user
    }
}


// ----------------------------------------  THUNKS  ----------------------------------------

export const getSingleUserThunk = userId => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const user = await response.json();
        dispatch(getSingleUserAction(user))
        return user
    }
}


// ----------------------------------------  REDUCER  ----------------------------------------

const userReducer = (state = {}, action) => {
    let newState
    switch (action.type) {
        case GET_SINGLE_USER:
            newState = {...state}
            newState[action.user.id] = action.user
            return newState
        default:
            return state
    }
}

export default userReducer
