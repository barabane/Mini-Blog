from flask_wtf import FlaskForm
from wtforms import EmailField, StringField
from wtforms.validators import DataRequired, Length, Email


class EditProfileForm(FlaskForm):
    username = StringField(validators=[Length(max=20, message="Длинна username должна быть не больше 20 символов")])
    email = EmailField(validators=[DataRequired(message="Введите Email"), Email(message="Введите корректный Email")])
    about = StringField(validators=[Length(max=200, message="Максимальная длинна описания 200 символов")])
