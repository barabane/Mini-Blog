from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import EqualTo, DataRequired, InputRequired, Length, Email


class SignUpForm(FlaskForm):
    email = EmailField(label='Email',
                       validators=[DataRequired(message="Введите Email"), InputRequired(message="Введите Email"),
                                   Email(message="Введите корректный Email")], default='')
    password = PasswordField('Пароль', validators=[InputRequired(message="Введите пароль"),
                                                   EqualTo('confirm_password', message="Пароли не совпадают"),
                                                   Length(min=7, message="Минимальная длинна пароля 7 символов")])
    confirm_password = PasswordField('Повторите пароль', validators=[InputRequired(message="Введите пароль еще раз"),
                                                                     Length(min=7,
                                                                            message="Минимальная длинна пароля 7 символов")])
