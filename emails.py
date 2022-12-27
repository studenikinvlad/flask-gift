from flask_mail import Message
from main import mail

def send_mail(subject, text_body):
    msg = Message(subject, sender="testov000@yandex.ru", recipients=['studenikin02@gmail.com'])
    msg.body = text_body
    mail.connect()
    mail.send(msg)