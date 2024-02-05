from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_handler():
    return 'login'


@auth.route('/signup', methods=['GET', 'POST'])
def signup_handler():
    return 'signup'
