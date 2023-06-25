from flask import Blueprint, request, jsonify
from app.models import Video, User
from ..models import db
import json


search_routes = Blueprint('search', __name__)

@search_routes.route('', methods=['POST'])
def search():
    """Returns the search results based on the query provided by the user"""

    # print('request.form ============>>>>>>>>>>>>', request.form)
    # print('request.json ============>>>>>>>>>>>>', request.json)
    # print('request.get_json() ============>>>>>>>>>>>>', request.get_json())
    # print('request.get_json ============>>>>>>>>>>>>', request.get_json)
    # print('request.data ============>>>>>>>>>>>>', request.data)
    # print('request.json["query"] ============>>>>>>>>>>>>', request.json['query'])



    search_results = []

    # query = request.data.decode('utf-8')
    # print('query printing here ========>>>>>>>>', query)

    query = request.json['query']

    # query = body['query']
    # print('query printing here ========>>>>>>>>', query)

    videos = Video.query.filter(Video.name.ilike(f'%{query}%')).all()
    print('videos printing here ========>>>>>>>>', videos)


    users = User.query.filter(User.alias.ilike(f'%{query}%')).all()
    print('users printing here ========>>>>>>>>', users)

    search_results.extend([video.to_dict() for video in videos])
    search_results.extend([user.to_dict() for user in users])

    print('search_results printing here ========>>>>>>>>', search_results)

    # for result in search_results:
    #     print('result in for loop ============>>>>>>>>', result)
    #     result.to_dict()

    return { 'searchResults': search_results }
