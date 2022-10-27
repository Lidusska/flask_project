from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import g
from flask import flash

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms.validators import InputRequired

from .models import db
from .models import Article
from .models import User

import os


flask_app = Flask(__name__)

flask_app.config.from_pyfile("/vagrant/configs/default.py")

if "MDBLOG_CONFIG" in os.environ:
    flask_app.config.from_envvar("MDBLOG_CONFIG")

db.init_app(flask_app)

## FORMS
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[InputRequired()])
    new_password = PasswordFi