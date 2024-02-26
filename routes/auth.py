from flask import Blueprint, render_template, redirect, flash, g
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from UserLogin import UserLogin
from db import db
from forms.login_form import LoginForm
from forms.signup_form import SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_handler():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.get_user_by_email(form.email.data)
        if not user:
            return redirect('/login')

        if check_password_hash(pwhash=user.password, password=form.password.data):
            user_login = UserLogin().create(user)
            login_user(user_login, remember=True)
            return redirect("/")

        return redirect('/login')
    return render_template("login.html", form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup_handler():
    if g.user is not None and g.user.is_authenticated:
        return redirect('/')

    form = SignUpForm()

    if form.validate_on_submit():
        user = db.get_user_by_email(email=form.email.data)

        if user:
            flash("Такой пользователь уже существует")
            return render_template("signup.html", form=form)

        new_user = UserLogin().create(db.register_user(email=form.email.data, password=form.password.data))
        login_user(new_user, remember=True)
        return redirect("/feed/1")

    return render_template("signup.html", form=form)


@auth.route('/logout')
def logout_handler():
    logout_user()
    return redirect('/login')
