import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { useHistory, NavLink } from "react-router-dom";


function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory()
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push('/')
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
    <div className="dropdown">
      <button className="profile-button" onClick={openMenu}>
        {!user &&
            <div className='sign-up'>
                <i className="fa-solid fa-user-plus"></i>
                <h4>Sign In</h4>
            </div>
        }
        {user && user.profilePicture &&
            <img className='session-user-profile-picture' src={user.profilePicture}/>
        }
        {user && !user.profilePicture &&
            <h3 className='profile-icon'>{user?.username[0]}</h3>
        }
      </button>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <li>{`${user.firstName} ${user.lastName}`}</li>
            <li>{user.username}</li>
            <li>
              <NavLink onClick={closeMenu} to={`/users/${user.id}`}>Your Channel</NavLink>
            </li>
            <li>
              <button onClick={handleLogout}>Sign Out</button>
            </li>
          </>
        ) : (
          <div className="login-signup">
            <li>
                <OpenModalButton
                buttonText="Log In"
                onItemClick={closeMenu}
                modalComponent={<LoginFormModal />}
                />
            </li>

            <li>
                <OpenModalButton
                buttonText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal />}
                />
            </li>
          </div>
        )}
      </ul>
    </div>
    </>
  );
}

export default ProfileButton;
