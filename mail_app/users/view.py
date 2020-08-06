from flask import render_template, flash, Blueprint
from mail_app.users.form import LoginForm, SendMailForm
from mail_app.model.user import User
from mail_app import db, server
import logging

logging.basicConfig(level=logging.DEBUG)

user = Blueprint('user', __name__)


@user.route('/')
def home():
    form = LoginForm()
    return render_template('login.html', form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    logging.info(form.username.data)
    logging.info(form.passwd.data)
    user = User.query.filter_by(username=form.username.data)
    logging.info("user_count:", user.count())
    pw = User.query.filter_by(passwd=form.passwd.data)
    if user.count() == 0 and pw.count() == 0:
        flash('Invalid User')
        logging.info("if user is not present in db, insert into db")
        render_template('login.html', form=LoginForm())
        new_user = User(username=form.username.data, passwd=form.passwd.data)
        db.session.add(new_user)
        db.session.commit()
    else:
        form = SendMailForm()
        return render_template('send_mail.html', form=form)

    return render_template('login.html', form=form)


@user.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    form = SendMailForm()
    logging.info("Entry")
    From = form.sender.data
    Password = form.password.data
    To = form.recipient.data
    Subject = form.subject.data
    Body = form.body.data
    if form.validate_on_submit():
        logging.info("sending mail")
        server.login(From, Password)
        server.sendmail(From, To, Subject, Body)
        flash('Mail sent successfully')
    else:
        logging.info("mail couldn't send")
        flash('Invalid Email')
    return render_template('send_mail.html', form=form)

