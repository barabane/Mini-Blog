from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length


class AddPostForm(FlaskForm):
    title = StringField("Заголовок поста",
                        validators=[DataRequired(), Length(min=5, message="Минимальная длинна заголовка 5 символов"),
                                    Length(max=200, message="Максимальная длинна заголовка 200 символов")], default='')
    text = TextAreaField("Содержание поста",
                         validators=[DataRequired(), Length(min=200, message="Минимальная длинна поста 200 символов"),
                                     Length(max=2500, message="Максимальная длинна поста 2500 символов")], default='')
    hashtags = TextAreaField("Хештеги",
                             validators=[
                                 Length(max=50, message="Общая длинна хештегов должна быть меньше 50 символов")])
