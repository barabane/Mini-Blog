from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = StringField("Ваш комментарий", validators=[DataRequired()])
