// ----------------------------------------  ACTIONS  ----------------------------------------
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const SUBSCRIBE_UNSUBSCRIBE = 'session/SUBSCRIBE_UNSUBSCRIBE'

const setUser = (user) => ({
	type: SET_USER,
	payload: user,
});

const removeUser = () => ({
	type: REMOVE_USER,
});

const subscribeUnsubscribeAction = (user) => {
    return {
        type: SUBSCRIBE_UNSUBSCRIBE,
        payload: user
    }
}

const initialState = { user: null };

// ----------------------------------------  THUNKS  ----------------------------------------

export const authenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/", {
		headers: {
			"Content-Type": "application/json",
		},
	});
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const login = (email, password) => async (dispatch) => {
	const response = await fetch("/api/auth/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			email,
			password,
		}),
	});

	if (response.ok) {
		const data = await response.json();
        dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["Invalid login credentials."];
	}
};

export const logout = () => async (dispatch) => {
	const response = await fetch("/api/auth/logout", {
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (response.ok) {
		dispatch(removeUser());
	}
};

export const signUp = (formData) => async (dispatch) => {
    // for (let key of formData.entries()) {
    //     console.log('formData inside of the thunk', key[0] + '----->' + key[1]);
    //   }
	const response = await fetch("/api/auth/signup", {
		method: "POST",
		body: formData
	});
	if (response.ok) {
		const data = await response.json();
		dispatch(setUser(data));
		return null;
	} else if (response.status < 500) {
		const data = await response.json();
		if (data.errors) {
			return data.errors;
		}
	} else {
		return ["An error occurred. Please try again."];
	}
};

export const subscribeUnsubscribeThunk = (userId, currUserId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}/subscribe/${currUserId}`, {
        method: 'POST',
        body: userId, currUserId
    });
    if (response.ok) {
        const user = await response.json()
        dispatch(subscribeUnsubscribeAction(user))
    }
}

// ----------------------------------------  REDUCER  ----------------------------------------

export default function reducer(state = initialState, action) {
	switch (action.type) {
		case SET_USER:
			return { user: action.payload };
		case REMOVE_USER:
			return { user: null };
        case SUBSCRIBE_UNSUBSCRIBE:
            return { user: action.payload };
		default:
			return state;
	}
}
