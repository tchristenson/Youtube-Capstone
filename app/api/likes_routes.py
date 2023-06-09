from flask import Blueprint, request
from app.models import Video, User
from flask_login import current_user, login_required, current_user
from ..models import db


likes_routes = Blueprint('likes', __name__)
