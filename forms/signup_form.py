from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import EqualTo, InputRequired


class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(message="Введите Email")])
    password = PasswordField('Пароль', validators=[InputRequired(message="Введите пароль"),
                                                   EqualTo('repeat_password', message="Пароли не совпадают")])
    repeat_password = PasswordField('Повторите пароль', validators=[InputRequired(message="Введите пароль еще раз")])
