import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import styles from './LoginForm.module.css'

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  const handleDemoUser = () => {
    setEmail('georgecostanza@summerofgeorge.com')
    setPassword('password')
  }

  return (
    <div className={styles['login-form']}>
      <h1 className={styles["header"]}>Log In</h1>
      <form onSubmit={handleSubmit}>
        <ul className={styles['errors']}>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>

        <div className={styles["input"]}>
            <label>
            {`Email (required):`}
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
            {`Password (required):`}
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
            </label>
        </div>

        <div className={styles['buttons-container']}>
            <button
                className={email && password ? styles['submit-button-active'] : styles['submit-button']}
                disabled={email && password ? false : true}
                type="submit">Log In</button>
            <button className={styles['demo-user']} type="submit" onClick={handleDemoUser}>Demo User</button>
        </div>
      </form>

    </div>

  );
}

export default LoginFormModal;
