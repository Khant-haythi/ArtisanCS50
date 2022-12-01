from flask import Flask,session,render_template
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Userinfo.db"
db = SQLAlchemy(app)
# initialize the app with the extension
app.app_context().push()


#Define Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String,nullable=False)



@app.route('/')
def homepage():
    """Homepage"""
    return render_template("index.html")
    
@app.route('/register')
def register():
    "Register For Users"
    return render_template("register.html")