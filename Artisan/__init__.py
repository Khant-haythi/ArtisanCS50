from flask import Flask,session,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet,IMAGES,configure_uploads
import os

# create the app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/image/'
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///RegisterInfo.db"
app.config["SECRET_KEY"]  = 'c732e0a78014a029460243fd'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path,UPLOAD_FOLDER)

app.config['UPLOADED_PHOTO_DEST'] = 'uploads'
photos = UploadSet('photos',IMAGES)
configure_uploads(app,photos)
db = SQLAlchemy(app)
# initialize the app with the extension
app.app_context().push()
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
from Artisan import routes

