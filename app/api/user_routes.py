from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User
from ..models import db
from sqlalchemy import select
from ..models.subscribers import subscribers

user_routes = Blueprint('users', __name__)


@user_routes.route('')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
# @login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


## ----------------------------------------  SUBSCRIBE OR UNSUBSCRIBE FROM A USER  ----------------------------------------
@user_routes.route('/<int:target_user_id>/subscribe/<int:curr_user_id>', methods=['POST'])
@login_required
def subscribe_unsubscribe(target_user_id, curr_user_id):
    """Queries for a user, and subscribes the current user to that queried user.
    If the current user has already subscribed to the queried user, it unsubscribes the current user"""

    target_user = User.query.get(target_user_id)
    if not target_user:
        return {'error': 'user not found'}

    curr_user = User.query.get(curr_user_id)
    if not curr_user:
        return {'error': 'user not found'}

    query = select([subscribers]).where(
        (subscribers.c.followed_user_id == target_user_id) & (subscribers.c.following_user_id == curr_user_id)
    )

    result = db.session.execute(query)

    has_subscribed = result.fetchone() is not None

    if has_subscribed:
        curr_user.subscribed.remove(target_user)
        db.session.commit()
        return curr_user.to_dict()
    else:
        curr_user.subscribed.append(target_user)
        db.session.commit()
        return curr_user.to_dict()
