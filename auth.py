from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, redirect, flash
from flask_login import login_user, login_required, logout_user
from forms.login_form import LoginForm
from forms.signup_form import SignUpForm
from UserLogin import UserLogin
from db import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_handler():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.get_user_by_email(form.email.data)

        if not user:
            flash("Такого пользователя не существует")
            return redirect('/login')

        if check_password_hash(pwhash=user.password, password=form.password.data):
            user_login = UserLogin().create(user)
            login_user(user_login, remember=True)
            return redirect('/feed')

        flash("Неправильный логин/пароль")
        return redirect('/login')
    return render_template("login.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup_handler():
    form = SignUpForm()

    if form.validate_on_submit():
        user = db.get_user_by_email(email=form.email.data)

        if user:
            flash("Такой пользователь уже существует")
            return render_template("signup.html", form=form)

        new_user = UserLogin().create(db.register_user(email=form.email.data, password=form.password.data))
        login_user(new_user, remember=True)
        return redirect('/feed')

    return render_template("signup.html", form=form)


@auth.route('/logout')
@login_required
def logout_handler():
    logout_user()
    return redirect('/login')