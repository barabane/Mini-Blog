from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile_handler():
    return 'Profile'


@main.route('/feed')
@login_required
def feed_handler():
    return render_template("feed.html")