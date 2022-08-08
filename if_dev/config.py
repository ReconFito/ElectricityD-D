import secrets
import os

class Config(object):
    SECRET_KEY = secrets.token_hex()
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
    MAIL_DEFAULT_SENDER = os.environ.get("EMAIL_USER")
    # MAIL_DEFAULT_SENDER = ""
    # SESSION_COOKIE_SECURE = True