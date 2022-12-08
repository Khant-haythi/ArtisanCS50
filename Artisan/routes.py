from Artisan import app
from flask import render_template,request,redirect,url_for,flash
from Artisan.model import User
from Artisan.form import RegisterForm,LoginForm
from Artisan import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user
from Artisan.__init__ import LoginManager

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
    if form.errors != {} :
        for err_msg in form.errors.values():
            flash(f'There was an error when creating account : {err_msg}',category='danger')

    return render_template("register.html",form=form)




@app.route('/login',methods=["GET", "POST"])
def login():
    "Login For Users"

    form = LoginForm()
    if form.validate_on_submit():
        new_user= User.query.filter_by(username=form.username.data).first()
        if new_user and new_user.verify_password(attempted_password=form.password.data):
            login_user(new_user)
            flash(f'Logging In Successfully!',category='info')
            return redirect(url_for('crochet'))
        else:
            flash ('Username and Password are Incorrect.Please try again!!')


    return render_template("login.html",form=form)



@app.route('/crochet')
def crochet():
    "Crochet Page "
    return render_template('crochet.html')