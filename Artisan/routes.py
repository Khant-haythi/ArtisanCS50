from Artisan import app
from flask import render_template,request,redirect,url_for,flash
from Artisan.model import User
from Artisan.form import RegisterForm
from Artisan import db
from werkzeug.security import check_password_hash, generate_password_hash

@app.route('/')
def homepage():
    """Homepage"""
    return render_template("index.html")
    
@app.route("/register",methods=["GET", "POST"])
def register():
    "Register For Users"
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              password=generate_password_hash(form.password.data))
        db.session.add(user_to_create)
        db.session.commit()
        
        flash("Registration Successful")
        return redirect(url_for('homepage'))
       
    
    else:

        return render_template("register.html",form=form)

@app.route('/login')
def login():
    "Login For Users"
    return render_template("login.html")