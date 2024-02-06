from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
def main_handler():
    return render_template("main.html")


@main.route('/profile')
@login_required
def profile_handler():
    return 'Profile'