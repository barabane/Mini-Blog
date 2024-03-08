from flask import Blueprint, redirect, render_template, flash, url_for, abort
from flask_login import login_required, current_user
from loguru import logger

from db import db
from forms.add_post_form import AddPostForm
from forms.edit_profile_form import EditProfileForm

profile = Blueprint('profile', __name__, template_folder="templates")


@profile.route('/<username>', methods=["GET", "POST"])
# @profile.route('/<username>/publish', methods=["POST"])
@login_required
@logger.catch
def profile_handler(username):
    user = db.get_user_by_username(username)

    if not user:
        return redirect(url_for('main.index_handler'))

    form = AddPostForm()
    if form.validate_on_submit():
        if current_user.id == user.id:
            db.create_post(text=form.text.data, title=form.title.data, author_id=user.id)
            return redirect(url_for('profile.profile_handler', username=current_user.username, form=form))
        return abort(403)

    posts = db.get_user_posts(current_user.id)
    return render_template("profile.html", user=user, posts=posts, form=form)


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
        user_exists = db.get_user_by_username(new_username)

        if user_exists and new_username != current_user.username:
            flash("Этот username занят", category="error")
            return render_template("profile_edit.html", user=user, form=form)

        user = db.get_user_by_username(username)
        user.email = form.email.data
        user.username = form.username.data
        user.about = form.about.data

        db.update_user(updated_user=user)

        return redirect(f'/profile/{user.username}')

    return render_template("profile_edit.html", user=user, form=form)

# @profile.route('/publish/<user_id>', methods=["POST"])
# @login_required
# @logger.catch
# def publish_handler(user_id):
#     form = AddPostForm()
#
#     if form.validate_on_submit():
#
#     return redirect(url_for('profile.profile_handler', username=current_user.username, form=form))
