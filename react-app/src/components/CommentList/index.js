import EditDeleteCommentModal from "../EditDeleteCommentModal";
import OpenModalIcon from "../OpenModalIcon";
import LoginFormModal from "../LoginFormModal";
import styles from './CommentList.module.css'


function CommentList({video, commentsArr, sessionUser}) {

    return (
    <ul className={styles.container}>
        {commentsArr.map(comment => (
            <div key={comment.id}>
                <li>
                    <div className={styles['single-comment-container']}>
                        <img className={styles['profile-picture']} src={comment.user.profilePicture}/>
                        <div className={styles['comment-owner-info']}>
                            <p>{comment.user.username}</p>
                            <p>{comment.content}</p>
                        </div>

                        {sessionUser && (
                            <OpenModalIcon modalComponent={<EditDeleteCommentModal video={video} comment={comment}/>}></OpenModalIcon>
                        )}

                        {!sessionUser && (
                            <OpenModalIcon modalComponent={<LoginFormModal/>}></OpenModalIcon>
                        )}
                    </div>
                </li>
            </div>
        ))}
    </ul>
    )
}

export default CommentList
