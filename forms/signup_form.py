from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import EqualTo, DataRequired, InputRequired, Length, Email


class SignUpForm(FlaskForm):
    email = EmailField('Email',
                       validators=[DataRequired(message="Введите Email"), InputRequired(message="Введите Email"),
                                   Email(message="Введите корректный Email")])
    password = PasswordField('Пароль', validators=[InputRequired(message="Введите пароль"),
                                                   EqualTo('repeat_password', message="Пароли не совпадают"),
                                                   Length(min=7, message="Минимальная длинна пароля 7 символов")])
    repeat_password = PasswordField('Повторите пароль', validators=[InputRequired(message="Введите пароль еще раз"),
                                                                    Length(min=7,
                                                                           message="Минимальная длинна пароля 7 символов")])
