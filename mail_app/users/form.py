from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField


class LoginForm(FlaskForm):
    username = StringField('User Name:')
    passwd = PasswordField('Password:')
    submit = SubmitField('Login')


class SendMailForm(FlaskForm):
    sender = StringField('From:')
    password = PasswordField('Password:')
    recipient = StringField('To:')
    subject = StringField('Subject:')
    body = TextAreaField('Body:')
    send = SubmitField('Send')
