from Artisan import app,login_manager
from flask import render_template,request,redirect,url_for,flash,send_from_directory,url_for,session
from Artisan.model import User,Cards
from Artisan.form import RegisterForm,LoginForm,BlogPostForm
from Artisan import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user,current_user,login_required
from Artisan.__init__ import LoginManager
import os


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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login',methods=["GET", "POST"])
def login():
    "Login For Users"

    form = LoginForm()
    if form.validate_on_submit():
        register_user= User.query.filter_by(username=form.username.data).first()
        if register_user and register_user.verify_password(attempted_password=form.password.data):
            login_user(register_user)
            flash(f'Logging In Successfully!',category='info')
            session["user_id"] = register_user.id
            return redirect(url_for('blog'))
        else:
            flash ('Username and Password are Incorrect.Please try again!!')


    return render_template("login.html",form=form)

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route('/crochet')
def crochet():
    "Crochet Page "
    return render_template('crochet.html')


@app.route('/blog')
def blog():
    "Blog Post Page "
    #grab all the info from Cards database
    cards = Cards.query.order_by(Cards.created_date)
    return render_template('blog.html',cards=cards)

def save_image(photo_file):
    photo_name = photo_file.filename
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'],photo_name)
    photo_file.save(photo_path)
    return photo_name

#AddPost
@app.route('/createpost',methods=["GET","POST"])
@login_required
def createpost():
    "Create BLog Post Page "
    form = BlogPostForm()
    if form.validate_on_submit():
        owned_user = current_user.id
        title = form.title.data
        content = form.content.data
        author = form.author.data
        created_date = form.created_date.data
        image_name = save_image(form.image.data)
        image_url = url_for('static',filename='image/'+image_name)

        post = Cards(title=title,content=content,author=author,created_date=created_date,image_url=image_url,user_id=owned_user)

        db.session.add(post)
        db.session.commit()
        flash(f'Creating Post Successful!!',category='info')
    return render_template('createpost.html',form=form)

@app.route("/blog/delete/<int:id>", methods=["GET", "POST"])
@login_required
def deletePost(id):
    post_delete = Cards.query.get_or_404(id)
    id = current_user.id
    if id == post_delete.owned_user.id:
 
        try:
            db.session.delete(post_delete)
            db.session.commit()
 
            #Reply Successful Message
            flash(f'Blog Post Was Deleted!',category='warning')
            cards = Cards.query.order_by(Cards.created_date)
            return render_template('blog.html',cards=cards)
 
 
        except:
            #Reply Error Message
            flash ( f'There was a Problem when deleting Post!!!',category='danger')
            cards = Cards.query.order_by(Cards.created_date)
            return render_template('blog.html',cards=cards)

    else:
        flash(f'Only Allowed User can delete this post!!',category='danger')
        cards = Cards.query.order_by(Cards.created_date)
        return render_template('blog.html',cards=cards)

@app.route('/blog/edit/<int:id>',methods=["GET","POST"])
@login_required
def editPost(id):
    updatecard = Cards.query.get_or_404(id)
    form = BlogPostForm()
    id = current_user.id
    if form.validate_on_submit():
        updatecard.title = form.title.data
        updatecard.content = form.content.data
        updatecard.author = form.author.data
        updatecard.created_date = form.created_date.data
        image_name = save_image(form.image.data)
        updatecard.image_url = url_for('static',filename='image/'+image_name)

        db.session.commit()
        flash(f'Post Has Been Updated',category='warning')
        return render_template('editPost.html',form=form,id=updatecard.card_id)

    
    if id == updatecard.owned_user.id:

        form.title.data =  updatecard.title
        form.content.data = updatecard.content
        form.author.data = updatecard.author
        form.created_date.data = updatecard.created_date
        form.image.data = updatecard.image_url
        return render_template('editPost.html',form=form,id=updatecard.card_id)

    else:
        flash(f'Only Allow User can Edit post',category='warning')
        cards = Cards.query.order_by(Cards.created_date)
        return render_template('Blog.html',cards=cards)
            
#For Individual Blog Post Page
@app.route('/blog/<int:id>')
def showPost(id):
    blogpost = Cards.query.get_or_404(id)
    return render_template('blogPost.html',blogpost=blogpost)

    
        

  
