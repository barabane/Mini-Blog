from flask import Blueprint, render_template, redirect, flash, g
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from loguru import logger

from UserLogin import UserLogin
from db import db
from forms.login_form import LoginForm
from forms.signup_form import SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
@logger.catch
def login_handler():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            user = db.get_user_by_email(form.email.data)

            if not user:
                flash('Такого пользователя не существует', category='error')
                return redirect('/login')

            if check_password_hash(pwhash=user.password, password=form.password.data):
                user_login = UserLogin().create(user)
                login_user(user_login, remember=True)
                logger.info(f"User {user_login.get_id()} logged in")
                return redirect("/")

            flash('Неверный логин/пароль', category='error')
            return redirect('/login')
        return render_template("login.html", form=form)
    except Exception:
        flash('Что-то пошло не так, попробуйте снова')
        return redirect('/login')


@auth.route('/signup', methods=['GET', 'POST'])
@logger.catch
def signup_handler():
    try:
        if g.user is not None and g.user.is_authenticated:
            return redirect('/')

        form = SignUpForm()
        if form.validate_on_submit():
            user = db.get_user_by_email(email=form.email.data)

            if user:
                flash('Такой пользователь уже существует', category='error')
                return render_template("signup.html", form=form)

            new_user = UserLogin().create(db.register_user(email=form.email.data, password=form.password.data))
            login_user(new_user, remember=True)
            logger.success(f"New user signed up {current_user.id}")
            return redirect("/")
        return render_template("signup.html", form=form)
    except Exception:
        flash('Что-то пошло не так, попробуйте снова')
        return redirect('/signup')


@auth.route('/logout')
@login_required
@logger.catch
def logout_handler():
    logger.info(f"User {current_user.id} logged out")
    logout_user()
    return redirect('/login')
