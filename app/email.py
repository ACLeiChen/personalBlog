from threading import Thread
from flask import current_app, render_template
from flask.ext.mail import Message
from . import mail
import requests

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# def send_email(to, subject, template, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr


def send_simple_message(to, subject, plaintext, html):
    print('222')
    return requests.post(
        "https://api.mailgun.net/v3/sandboxb482a07aead94239ae4170a164d06de2.mailgun.org/messages",
        auth=("api", "key-8368897899de58afdf3f499372e71d14"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxb482a07aead94239ae4170a164d06de2.mailgun.org>",
              "to": to,
              "subject": subject,
              "text": plaintext,
              "html": html
              }
    )

def send_email(to, subject, template, **kwargs):
    print('111')
    thr = Thread(target=send_simple_message, args=[to, subject, render_template(template + '.txt', **kwargs), render_template(template + '.html', **kwargs)])
    print('333')
    thr.start()
    print('444')
    return thr