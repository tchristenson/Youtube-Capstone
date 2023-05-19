import EditDeleteCommentModal from "../EditDeleteCommentModal";
import OpenModalIcon from "../OpenModalIcon";
import LoginFormModal from "../LoginFormModal";


function CommentList({video, commentsArr, sessionUser}) {

    return (
        <ul className="comment-container">
        {commentsArr.map(comment => (
            <div key={comment.id}>
                <li>
                    <div>
                        {comment.content}

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
