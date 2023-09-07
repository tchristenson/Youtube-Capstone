from flask import Blueprint, request, jsonify
from app.models import Video, User
from ..models import db
import json


search_routes = Blueprint('search', __name__)

@search_routes.route('', methods=['POST'])
def search():
    """Returns the search results based on the query provided by the user"""

    search_results = []

    query = request.json['query']

    # print('query printing here ========>>>>>>>>', query)

    videos = Video.query.filter(Video.name.ilike(f'%{query}%')).all()
    # print('videos printing here ========>>>>>>>>', videos)

    users = User.query.filter(User.username.ilike(f'%{query}%')).all()
    # print('users printing here ========>>>>>>>>', users)
    for user in users:
        user_videos = Video.query.filter_by(user_id=user.id).all()
        # print('user_videos printing here ========>>>>>>>>', user_videos)
        search_results.extend([video.to_dict() for video in user_videos])

    search_results.extend([video.to_dict() for video in videos])

    # print('search_results printing here ========>>>>>>>>', search_results)

    return { 'searchResults': search_results }
