from flask_mail import Message
from flask import render_template, current_app
from threading import Thread
from if_dev import mail

def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, recipient, template, **kwargs):
    msg = Message(subject, recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    thrd = Thread(target=async_send_mail, args=[current_app._get_current_object(), msg])
    thrd.start()
    return thrd