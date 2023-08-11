
// ----------------------------------------  ACTIONS  ----------------------------------------
const SEARCH_VIDEOS_USERS = 'search/searchVideosUsers'
const CLEAR_SEARCH_RESULTS = 'search/clearSearchResults'

const searchVideosUsersAction = (payload) => {
    return {
        type: SEARCH_VIDEOS_USERS,
        payload
    }
}

const clearSearchResultsAction = (payload) => {
    return {
        type: CLEAR_SEARCH_RESULTS,
        payload
    }
}

// ----------------------------------------  THUNKS  ----------------------------------------
export const searchVideosUsersThunk = (query) => async (dispatch) => {
    // console.log('query inside thunk ------->', query)
    const response = await fetch('/api/search', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            query: query
        })
    })
    if (response.ok) {
        // console.log('response', response)
        const searchResults = await response.json()
        // console.log('checking if this is running in between response from backend and action')
        // console.log('searchResults from backend after response.json ------->', searchResults)
        dispatch(searchVideosUsersAction(searchResults))
        return searchResults
    }
}

export const clearSearchResultsThunk = () => async (dispatch) => {
    dispatch(clearSearchResultsAction({}))
}


// ----------------------------------------  REDUCER  ----------------------------------------
const searchReducer = (state = {}, action) => {
    let newState;
    switch (action.type) {
        case SEARCH_VIDEOS_USERS:
            newState = {...state}
            let id = 1;
            // console.log('action.payload inside reducer', action.payload)
            action.payload.searchResults.forEach(item => {
              newState[id] = item;
              id += 1;
            //   console.log('newState inside for loop --->', newState)
            });
            return newState
        case CLEAR_SEARCH_RESULTS:
            newState = {...state}
            newState = action.payload
            return newState
        default:
            return state
    }
}

export default searchReducer
