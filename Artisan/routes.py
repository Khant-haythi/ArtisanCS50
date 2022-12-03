from Artisan import app
from flask import render_template,request
from Artisan.model import User

@app.route('/')
def homepage():
    """Homepage"""
    return render_template("index.html")
    
@app.route("/register",methods=["GET", "POST"])
def register():
    "Register For Users"
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Ensure username was submitted
        if not username:
            flash ("Please enter username!!")
        elif not password:
            flash("Please enter password")
        elif not confirmation:
            flash("Please enter confirmation")
        
        if password != confirmation:
            flash("Your password is not match with the confirmation.Please try again")

        hash = generate_password_hash(password)
        user = User(
            username=request.form["username"],
            password=generate_password_hash(request.form["password"]),
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))
    else:

        return render_template("register.html")

@app.route('/login')
def login():
    "Login For Users"
    return render_template("login.html")