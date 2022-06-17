from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Search(FlaskForm):
    type = StringField(label='Type:', validators=[DataRequired()])
    mood = StringField(label='Genre:', validators=[DataRequired()])
    submit = SubmitField(label='Submit')