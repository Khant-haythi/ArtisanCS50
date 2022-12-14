from Artisan import app
from flask import render_template,request,redirect,url_for,flash,send_from_directory,url_for
from Artisan.model import User
from Artisan.form import RegisterForm,LoginForm
from Artisan import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user
from Artisan.__init__ import LoginManager
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

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


@app.route('/blog')
def blog():
    "Crochet Page "
    return render_template('blog.html')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)

@app.route('/uploadimage',method=['GET','POST'])
def upload_image():
    form = ImageUploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file',filename=filename)
    return render_template('uploadimage.html',form=form,file_url=file_url)


@app.route('/createpost',methods=["GET", "POST"])
def Create():
    "Place to create posts for user "
    form = ImageUploadForm()
    if request.method=='POST':
        upload_image=request.files['upload_image']
 
        if upload_image.filename != '':
            post_image=secure_filename(upload_image.filename)
            filepath=os.path.join(app.config['UPLOAD_FOLDER'] ,upload_image.filename)
            print(filepath)
            upload_image.save(os.path.join(app.config['UPLOAD_FOLDER'] ,post_image))
            return render_template('createpost.html',path=filepath)
            flash(f'Image Upload Successfully',category='info')
       
    return render_template('createpost.html')


