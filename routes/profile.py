from loguru import logger

from flask import Blueprint, redirect, render_template, flash, url_for
from flask_login import login_required

from db import db
from forms.edit_profile_form import EditProfileForm

profile = Blueprint('profile', __name__, template_folder="templates")


@profile.route('/<username>')
@login_required
@logger.catch
def profile_handler(username):
    user = db.get_user_by_username(username)

    if not user:
        return redirect(url_for('main.index_handler'))

    return render_template("profile.html", user=user)


@profile.route('/<username>/edit', methods=['GET', 'POST'])
@login_required
@logger.catch
def profile_edit_handler(username):
    user = db.get_user_by_username(username)

    if not user:
        return redirect(url_for('main.index_handler'))

    form = EditProfileForm()
    if form.validate_on_submit():
        new_username = form.username.data

        if db.get_user_by_username(new_username):
            flash("Этот username занят", category="error")
            return render_template("profile_edit.html", user=user, form=form)

        user = db.get_user_by_username(username)
        user.email = form.email.data
        user.username = form.username.data
        user.about = form.about.data

        db.update_user()

        return redirect(f'/profile/{user.username}')

    return render_template("profile_edit.html", user=user, form=form)
