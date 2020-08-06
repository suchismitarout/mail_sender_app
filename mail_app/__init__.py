from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import smtplib
import os
import logging

app = Flask(__name__)

###################
# DATABASE SETUP  #
###################

base_dir = os.path.abspath(os.path.dirname(__file__))
logging.info("======")
logging.info(base_dir)
logging.info("======")
app.config['SECRET_KEY'] = 'myseckey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



######################
# MAIL SERVER SETUP  #
######################

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

######################
# REGISTER BLUEPRINT #
######################

from mail_app.users.view import user

app.register_blueprint(user)
