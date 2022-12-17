from flask import Flask,session,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# create the app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/image'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ArtisanInfo.db"
app.config["SECRET_KEY"]  = 'c732e0a78014a029460243fd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path,UPLOAD_FOLDER)

db = SQLAlchemy(app)
# initialize the app with the extension
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
from Artisan import routes

with app.app_context():
    db.create_all()