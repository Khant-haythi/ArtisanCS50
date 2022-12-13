from flask import Flask,session,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///RegisterInfo.db"
app.config["SECRET_KEY"]  = 'c732e0a78014a029460243fd'
app.config['UPLOAD_FOLDER'] = "static/image/"
db = SQLAlchemy(app)
# initialize the app with the extension
app.app_context().push()
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
from Artisan import routes


