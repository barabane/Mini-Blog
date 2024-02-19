from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length


class AddPostForm(FlaskForm):
    title = StringField("Заголовок поста", validators=[DataRequired()])
    text = TextAreaField("Содержание поста", validators=[DataRequired()])
    hashtags = TextAreaField("Хештеги",
                             validators=[
                                 Length(max=50, message="Общая длинна хештегов должна быть меньше 50 символов")])
