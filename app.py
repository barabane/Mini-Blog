import os

from dotenv import load_dotenv
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from loguru import logger

from db import db
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes.profile import profile as profile_blueprint

load_dotenv()

logger.add("logs/user.log", format="{time} | {level} | {message}", rotation="1 day", compression="zip")


def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    with app.app_context():
        app.config['CSRF_ENABLED'] = True
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(profile_blueprint, url_prefix="/profile")

        # @app.errorhandler(404)
        # @login_required
        # def page_not_found_logged_in(error):
        #     return redirect('/')

        # @app.before_request
        # def before_request():

        @login_manager.user_loader
        def load_user(user_id):
            return db.get_user_by_id(user_id=user_id)

        @login_manager.unauthorized_handler
        def unauthorized():
            return redirect(url_for('main.index_handler'))

    return app


app_ready = create_app()
