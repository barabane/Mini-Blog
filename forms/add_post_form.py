from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, InputRequired


class AddPostForm(FlaskForm):
    title = StringField("Заголовок поста", validators=[DataRequired()])
    text = TextAreaField("Содержание поста", validators=[DataRequired()])
