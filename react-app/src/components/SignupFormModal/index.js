import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import { useEffect } from "react";
import styles from './SignupForm.module.css'

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [about, setAbout] = useState("")
    const [profilePicture, setProfilePicture] = useState("")
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
    const [validationErrors, setValidationErrors] = useState([]);
    const [hasSubmitted, setHasSubmitted] = useState(false);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
            if (validationErrors.length) return alert('Your Post has errors, cannot submit!')

            const formData = new FormData()
            formData.append('email', email)
            formData.append('username', username)
            formData.append('first_name', firstName)
            formData.append('last_name', lastName)
            formData.append('about', about)
            formData.append('profile_picture', profilePicture)
            formData.append('password', password)

            for (let key of formData.entries()) {
                console.log('formData inside of the thunk', key[0] + '----->' + key[1]);
              }

			const data = await dispatch(signUp(formData));
			if (data) {
				setErrors(data);
			} else {

				closeModal();
			}
		} else {
			setErrors([
				"Confirm Password field must be the same as the Password field",
			]);
		}
	};

    useEffect(() => {
        const errors = [];
        // Only adding to the validation errors for fields that are nullable=False in the Video model
        if (!email) errors.push('Email required')
        if (!username) errors.push('Username required')
        if (!password) errors.push('Password required')
        if (!firstName) errors.push('First name required')
        if (!lastName) errors.push('Last name required')
        setValidationErrors(errors)
    }, [email, username, password, firstName, lastName])

	return (
        <div className={styles['signup-form']}>
			<h1>Sign Up</h1>
			<form
                onSubmit={handleSubmit}
                encType="multipart/form-data"
            >
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<label>
					Email
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					Username
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label>
					Password
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
                <label>
					First Name
					<input
						type="text"
						value={firstName}
						onChange={(e) => setFirstName(e.target.value)}
						required
					/>
				</label>
                <label>
					Last Name
					<input
						type="text"
						value={lastName}
						onChange={(e) => setLastName(e.target.value)}
						required
					/>
				</label>
                <label>
					About
					<input
						type="textarea"
						value={about}
						onChange={(e) => setAbout(e.target.value)}
					/>
				</label>

                <div>
                    <label>Profile Picture</label>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={(e) => setProfilePicture(e.target.files[0])}
                        >
                    </input>
                </div>

				<button type="submit">Sign Up</button>
			</form>

        </div>

	);
}

export default SignupFormModal;
