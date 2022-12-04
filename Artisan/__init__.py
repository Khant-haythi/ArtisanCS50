from flask import Flask,session,render_template,flash,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///RegisterInfo.db"
app.config["SECRET_KEY"]  = 'c732e0a78014a029460243fd'
db = SQLAlchemy(app)
# initialize the app with the extension
app.app_context().push()

from Artisan import routes