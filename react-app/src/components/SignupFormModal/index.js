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
            formData.append('email', email.trim())
            formData.append('username', username.trim())
            formData.append('first_name', firstName.trim())
            formData.append('last_name', lastName.trim())
            formData.append('about', about.trim())
            formData.append('profile_picture', profilePicture)
            formData.append('password', password.trim())

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
        if (!email.trim()) errors.push('Email required')
        if (!username.trim()) errors.push('Username required')
        if (!password.trim()) errors.push('Password required')
        if (!firstName.trim()) errors.push('First name required')
        if (!lastName.trim()) errors.push('Last name required')
        setValidationErrors(errors)
    }, [email, username, password, firstName, lastName])

	return (
        <div className={styles['signup-form']}>
			<h1 className={styles["header"]}>Sign Up</h1>
			<form
                onSubmit={handleSubmit}
                encType="multipart/form-data"
            >
				<ul className={styles['errors']}>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>

                <div className={styles["input"]}>
                    <label>
                    {'Email (required):'}
                        <input
                            type="text"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                    {'Username (required):'}
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                    {'Password (required):'}
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                    {'Confirm Password (required):'}
                        <input
                            type="password"
                            value={confirmPassword}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                    {'First Name (required):'}
                        <input
                            type="text"
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                    {'Last Name (required):'}
                        <input
                            type="text"
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            required
                        />
                    </label>
                </div>

                <div className={styles["input"]}>
                    <label>
                        About
                        <textarea
                            type="textarea"
                            value={about}
                            onChange={(e) => setAbout(e.target.value)}
                        />
                    </label>
                </div>

                <div className={styles["profile-picture"]}>
                    <label>Profile Picture</label>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={(e) => setProfilePicture(e.target.files[0])}
                        >
                    </input>
                </div>

            <div className={styles['buttons-container']}>
                <button className={styles['cancel-button']} onClick={(e) => {
                    e.preventDefault(); setEmail(''); setUsername(''); setPassword('');
                    setFirstName(''); setLastName(''); setAbout(''); setProfilePicture('');
                    closeModal() }}
                    type="submit">Cancel</button>
                <button
                    className={email.trim() && username.trim() && password.trim() && firstName.trim() && lastName.trim() ? styles['submit-button-active'] : styles['submit-button']}
                    disabled={email.trim() && username.trim() && password.trim() && firstName.trim() && lastName.trim() ? false : true}
                    type="submit">Sign Up</button>

            </div>

			</form>

        </div>

	);
}

export default SignupFormModal;
