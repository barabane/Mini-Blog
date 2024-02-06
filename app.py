import os
from dotenv import load_dotenv
from flask_login import LoginManager
from flask import Flask
from UserLogin import UserLogin

from auth import auth as auth_blueprint
from main import main as main_blueprint

load_dotenv()


def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)

    with app.app_context():

        app.config['CSRF_ENABLED'] = True
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)

        @login_manager.user_loader
        def load_user(user_id):
            print('user_id')
            return UserLogin().get_user_from_db(user_id)

        @login_manager.unauthorized_handler
        def unauthorized():
            return "unauthorized"

        app.run(debug=True)

    return app


create_app()
