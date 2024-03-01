from flask import Blueprint, render_template, redirect, flash, g, url_for
from flask_login import login_user, logout_user, login_required, current_user
from loguru import logger
from werkzeug.security import check_password_hash

from UserLogin import UserLogin
from db import db
from forms.login_form import LoginForm
from forms.signup_form import SignUpForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
@logger.catch
def login_handler():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('main.index_handler'))

        form = LoginForm()
        if form.validate_on_submit():
            user = db.get_user_by_email(form.email.data)

            if not user:
                flash('Такого пользователя не существует', category='error')
                return redirect(url_for('auth.login_handler'))

            if check_password_hash(pwhash=user.password, password=form.password.data):
                user_login = UserLogin().create(user)
                login_user(user_login, remember=True)
                logger.info(f"User {user_login.get_id()} logged in")
                return redirect(url_for('main.index_handler'))

            flash('Неверный логин/пароль', category='error')
            return redirect(url_for('auth.login_handler'))
        return render_template("login.html", form=form)
    except Exception as ex:
        flash('Что-то пошло не так, попробуйте снова')
        logger.error(ex)
        return redirect(url_for('auth.login_handler'))


@auth.route('/signup', methods=['GET', 'POST'])
@logger.catch
def signup_handler():
    try:
        if g.user is not None and g.user.is_authenticated:
            return redirect(url_for('main.index_handler'))

        form = SignUpForm()
        if form.validate_on_submit():
            user = db.get_user_by_email(email=form.email.data)

            if user:
                flash('Такой пользователь уже существует', category='error')
                return render_template("signup.html", form=form)

            new_user = UserLogin().create(db.register_user(email=form.email.data, password=form.password.data))
            login_user(new_user, remember=True)
            logger.success(f"New user signed up {new_user.id}")
            return redirect(url_for('main.index_handler'))
        return render_template("signup.html", form=form)
    except Exception as ex:
        flash('Что-то пошло не так, попробуйте снова')
        logger.error(ex)
        return redirect(url_for('auth.signup_handler'))


@auth.route('/logout')
@login_required
@logger.catch
def logout_handler():
    logger.info(f"User {current_user.id} logged out")
    logout_user()
    return redirect(url_for('main.index_handler'))
