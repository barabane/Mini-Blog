import os
from dotenv import load_dotenv
from flask import Flask

from auth import auth as auth_blueprint
from main import main as main_blueprint

load_dotenv()


def create_app():
    app = Flask(__name__)

    with app.app_context():

        app.config['CSRF_ENABLED'] = True
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)

        app.run(debug=True)

    return app


create_app()
