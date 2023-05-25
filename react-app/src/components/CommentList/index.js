import EditDeleteCommentModal from "../EditDeleteCommentModal";
import { useModal } from "../../context/Modal";
import OpenModalIcon from "../OpenModalIcon";
import LoginFormModal from "../LoginFormModal";
import styles from './CommentList.module.css'
import { NavLink } from "react-router-dom";
import { useState } from "react";


function CommentList({video, commentsArr, sessionUser}) {

    const [isEditing, setIsEditing] = useState(false)
    const [editedCommentId, setEditedCommentId] = useState(null);

    return (
    <ul className={styles.container}>
        {commentsArr.map(comment => (
            <div key={comment.id}>
                <li>
                    <div className={styles['single-comment-container']}>
                        <NavLink to={`/channels/${comment.user.id}`}>
                            { comment.user.profilePicture ? (
                                <img className={styles['profile-picture']} src={comment.user.profilePicture}/>
                            ) : (
                                <h3 className={styles['profile-icon']}>{comment.user.username[0]}</h3>
                            )}
                        </NavLink>
                        <div className={styles['comment-owner-info']}>
                            <p>{comment.user.username}</p>

                            {isEditing && editedCommentId === comment.id? (
                                <form>
                                    <input className={styles['comment-input-active']} type='text' placeholder={comment.content}/>
                                </form>
                            ) : (
                                <form>
                                    <input className={styles['comment-input-inactive']} type='text' placeholder={comment.content}/>
                                </form>

                            )}
                        </div>


                        {sessionUser &&
                            <div className={styles['edit-comment-icon']}>
                                <OpenModalIcon modalComponent={<EditDeleteCommentModal comment={comment} setEditedCommentId={setEditedCommentId} setIsEditing={setIsEditing}/>}></OpenModalIcon>
                            </div>
                        }

                        {!sessionUser &&
                            <div className={styles['edit-comment-icon']}>
                                <OpenModalIcon modalComponent={<LoginFormModal/>}></OpenModalIcon>
                            </div>}
                    </div>
                </li>
            </div>
        ))}
    </ul>
    )
}

export default CommentList
