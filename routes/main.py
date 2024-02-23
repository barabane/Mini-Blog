from math import ceil

from flask import Blueprint, render_template, redirect, request
from flask_login import login_required

from db import db
from models.Posts import Posts

main = Blueprint('main', __name__)


@main.route('/feed/<int:page>')
@login_required
def feed_handler(page: int):
    posts = db.get_all_posts(limit=5, page=page)
    posts_qty = db.get_posts_qty()
    hashtags = db.get_all_hashtags()

    return render_template("feed.html", posts=posts, hashtags=hashtags,
                           pages_qty=ceil(posts_qty / 5), active_page=page)


@main.route('/post/<post_id>')
@login_required
def post_handler(post_id):
    post: Posts = db.get_post(post_id)
    hashtags = db.get_post_hashtags(post_id)
    author = db.get_user_by_id(post.author_id)
    post_comments = db.get_all_post_comments(post_id)

    return render_template("post.html", post=post, author=author.email, hashtags=hashtags,
                           comments=post_comments)


@main.route('/add_comment/<path:comment_info>', methods=['POST'])
@login_required
def add_comment_handler(comment_info):
    form = request.form
    post_id, author_id = comment_info.split('/')

    db.create_comment(text=form.get('comment'), post_id=post_id, author_id=author_id)
    return redirect(f'/post/{post_id}')