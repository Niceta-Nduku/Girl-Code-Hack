# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):

    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')
        
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/')

    from .opportunities import opportunity as opportunity_blueprint
    app.register_blueprint(opportunity_blueprint, url_prefix='/opportunities')

    from .institution import institution as institution_blueprint
    app.register_blueprint(institution_blueprint, url_prefix='/institution')

    from .student import student as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')

    from .professional import professional as professional_blueprint
    app.register_blueprint(professional_blueprint, url_prefix='/professional')

    return app
