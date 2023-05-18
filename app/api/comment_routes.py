from flask import Blueprint, request
from app.models import Comment, User, Video
from flask_login import current_user, login_required, current_user
from ..forms.comment_form import NewComment
from ..models import db

comment_routes = Blueprint('comments', __name__)

## ----------------------------------------  POST A COMMENT  ----------------------------------------
@comment_routes.route('/new', methods=['POST'])
@login_required
def add_comment():
    """Allows a logged in user to add a comment to a video"""

    form = NewComment()
    form['csrf_token'].data = request.cookies['csrf_token']

    print("form.data inside New Comment route ======>>", form.data)

    if form.validate_on_submit():

        comment = Comment(
            user_id = current_user.id,
            video_id = form.data['video_id'],
            content = form.data['content']
        )

        db.session.add(comment)
        db.session.commit()
        return comment.to_dict()

    return { "errors": form.errors }


## ----------------------------------------  GET COMMENTS BY VIDEO ID  ----------------------------------------
@comment_routes.route('/<int:id>', methods=['GET'])
def get_comments_by_video_id(id):
    """Returns all comments for a specific video"""

    print('Checking if I am inside the get_comments_by_video_id route')
    print('id ==============>>>>>>>>>>>>>>>>>>>>', id)
    comments = Comment.query.filter(Comment.video_id == Video.id).all()
    print('comments ==============>>>>>>>>>>>>>>>>>>>>', comments)

    if comments is None or len(comments) == 0:
        return {'Comments': []}

    return {'Comments': [comment.to_dict() for comment in comments]}
