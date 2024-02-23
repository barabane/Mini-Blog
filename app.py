import os

from dotenv import load_dotenv
from flask import Flask, g, redirect
from flask_login import LoginManager, current_user, login_required

from UserLogin import UserLogin
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes.profile import profile as profile_blueprint

load_dotenv()

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    app.config['CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(profile_blueprint)


    @app.errorhandler(404)
    def page_not_found(error):
        return redirect('/login')


    @app.errorhandler(404)
    @login_required
    def page_not_found_logged_in(error):
        return redirect('/feed/1')


    @app.before_request
    def before_request():
        g.user = current_user


    @login_manager.user_loader
    def load_user(user_id):
        return UserLogin().get_user_from_db(user_id)


    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect('/login')
