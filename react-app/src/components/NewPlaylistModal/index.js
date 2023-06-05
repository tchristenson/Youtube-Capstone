import React, { useEffect, useState, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import styles from './NewPlaylistModal.module.css'
import { useModal } from '../../context/Modal';

function NewPlaylistModal({video}) {

    const dispatch = useDispatch()
    const { closeModal } = useModal();
    const sessionUser = useSelector(state => state.session.user)

    console.log('video inside NewPlaylistModal', video)
    console.log('sessionUser inside NewPlaylistModal', sessionUser)


    return (
        <div className={styles["new-playlist-form"]}>
            <h4 className={styles["header"]}>Save to...</h4>
            <div className={styles["new-playlist-button-container"]}>
                <i id={styles['playlist-plus']} className="fa-solid fa-plus"></i>
                <button className={styles['new-playlist-button']}>
                    Create New Playlist
                </button>
            </div>

        </div>
    )

}

export default NewPlaylistModal
