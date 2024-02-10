from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user

from db import db
from forms.add_post_form import AddPostForm
from models.Post import Post

main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile_handler():
    return render_template("profile.html")


@main.route('/feed', methods=['GET', 'POST'])
@login_required
def feed_handler():
    form = AddPostForm()

    if form.validate_on_submit():
        user = db.get_user_by_id(current_user.get_id())

        db.create_post(author=user.email, title=form.title.data, text=form.text.data)
        return redirect(location='/feed')

    posts = db.get_all_posts()
    return render_template("feed.html", posts=posts, form=form)


@main.route('/post/<post_id>')
@login_required
def post_handler(post_id):
    post: Post = db.get_post(post_id)
    post_comments = db.get_all_post_comments(post_id)

    return render_template("post.html", post=post, comments=post_comments)


@main.route('/add_comment/<path:comment_info>', methods=['POST'])
@login_required
def add_comment_handler(comment_info):
    form = request.form
    post_id, author = comment_info.split('/')

    db.create_comment(text=form.get('comment'), post_id=post_id, author=author)
    return redirect(f'/post/{post_id}')
