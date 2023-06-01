
// ----------------------------------------  ACTIONS  ----------------------------------------
const GET_SINGLE_USER = 'users/GET_SINGLE_USER'
const GET_ALL_USERS = 'users/GET_ALL_USERS'
// const SUBSCRIBE_UNSUBSCRIBE = 'users/SUBSCRIBE_UNSUBSCRIBE'


const getSingleUserAction = (user) => {
    return {
        type: GET_SINGLE_USER,
        user
    }
}

const getAllUsersAction = (users) => {
    return {
        type: GET_ALL_USERS,
        users
    }
}

// const subscribeUnsubscribeAction = (user) => {
//     return {
//         type: SUBSCRIBE_UNSUBSCRIBE,
//         user
//     }
// }


// ----------------------------------------  THUNKS  ----------------------------------------

export const getSingleUserThunk = userId => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const user = await response.json();
        dispatch(getSingleUserAction(user))
        return user
    }
}

export const getAllUsersThunk = () => async (dispatch) => {
    const response = await fetch(`/api/users`)
    if (response.ok) {
        const users = await response.json()
        dispatch(getAllUsersAction(users))
        return users
    }
}

// export const subscribeUnsubscribeThunk = (userId, currUserId) => async (dispatch) => {
//     const response = await fetch(`/api/users/${userId}/subscribe/${currUserId}`, {
//         method: 'POST',
//         body: userId, currUserId
//     });
//     if (response.ok) {
//         const user = await response.json()
//         dispatch(subscribeUnsubscribeAction(user))
//     }
// }


// ----------------------------------------  REDUCER  ----------------------------------------

const userReducer = (state = {}, action) => {
    let newState
    switch (action.type) {
        case GET_SINGLE_USER:
            newState = {...state}
            newState[action.user.id] = action.user
            return newState
        case GET_ALL_USERS:
            newState = {...state}
            action.users.users.forEach(user => newState[user.id] = user)
            return newState
        // case SUBSCRIBE_UNSUBSCRIBE:
        //     newState = {...state}
        //     console.log('action.user inside Reducer', action.user)
        //     newState[action.user.id] = action.user
        //     return newState
        default:
            return state
    }
}

export default userReducer
