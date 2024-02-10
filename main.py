from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user

from db import db
from forms.add_post_form import AddPostForm
from models.Post import Post

main = Blueprint('main', __name__)


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_handler():
    form = AddPostForm()

    if form.validate_on_submit():
        db.create_post(text=form.text.data, title=form.title.data, author=current_user.email)
        return redirect('/profile')

    posts = db.get_user_posts(current_user.email)
    return render_template("profile.html", posts=posts, form=form)


@main.route('/feed')
@login_required
def feed_handler():
    posts = db.get_all_posts()
    return render_template("feed.html", posts=posts)


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
