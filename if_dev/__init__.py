#! /usr/bin/python3.10
from flask import Flask
from flask_mail import Mail
from if_dev.config import Config
import os

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()
    
    mail.init_app(app)

    from if_dev.routes import main
    from if_dev.errors.handlers import errors
    
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
