from uuid import uuid4

from flask import Blueprint, redirect, render_template
from flask_login import login_required, current_user

from db import db
from forms.add_post_form import AddPostForm

profile = Blueprint('profile', __name__)


@profile.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_handler():
    form = AddPostForm()

    if form.validate_on_submit():
        db.create_post(post_id=str(uuid4()), text=form.text.data, title=form.title.data, author_id=current_user.id,
                       hashtags=form.hashtags.data)
        return redirect('/profile')

    posts = db.get_user_posts(current_user.id)
    hashtags = db.get_all_hashtags()

    return render_template("profile.html", posts=posts, hashtags=hashtags, form=form)


@profile.route('/profile/delete/<post_id>')
@login_required
def delete_post_handler(post_id: str):
    post = db.get_post(post_id)

    if post.author_id != current_user.id:
        return redirect('/profile')

    db.delete_post(post_id)
    return redirect('/profile')
