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
    # septup enviroment variables for MAIL_ACCOUNT and MAIL_PASSWORD
    # app.config['MAIL_SERVER']='smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = "munozfito4@gmail.com"
    # app.config['MAIL_PASSWORD'] = "gxxvralbrgefxtsx"
    # app.config["MAIL_DEFAULT_SENDER"] = "munozfito4@gmail.com"
    # app.config['MAIL_USERNAME'] = os.getenv("MAIL_ACCOUNT")
    # app.config['MAIL_PASSWORD'] = os.getenv("MAILL_PASSWORD")
    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)

    from if_dev.routes import main
    from if_dev.errors.handlers import errors
    
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app