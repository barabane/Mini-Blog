from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),InputRequired(message="Введите Email")])
    password = PasswordField('Пароль', validators=[DataRequired(), InputRequired(message="Введите пароль")])
