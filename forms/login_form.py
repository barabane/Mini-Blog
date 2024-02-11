from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = EmailField('Email',
                       validators=[DataRequired(message="Введите Email"), InputRequired(message="Введите Email"),
                                   Email(message="Введите корректный Email")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Введите пароль"),
                                                   InputRequired(message="Введите пароль"),
                                                   Length(min=7, message="Минимальная длинна пароля 7 символов")])
