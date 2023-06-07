from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class NewPlaylist(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
