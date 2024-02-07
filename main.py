from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms.add_post_form import AddPostForm
from db import db

main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile_handler():
    return 'Profile'


@main.route('/feed', methods=['GET', 'POST'])
@login_required
def feed_handler():
    form = AddPostForm()

    if form.validate_on_submit():
        db.create_post(author_id=current_user.get_id(), title=form.title.data, text=form.text.data)
        posts = db.get_all_posts()

        # return render_template("feed.html", posts=posts, form=form)
        return redirect(location='/feed')

    posts = db.get_all_posts()
    return render_template("feed.html", posts=posts, form=form)