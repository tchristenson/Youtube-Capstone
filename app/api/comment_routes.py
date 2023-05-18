from flask import Blueprint, request
from app.models import Video, User
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
    return 'in process'
