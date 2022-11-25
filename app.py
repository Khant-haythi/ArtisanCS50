import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a registration form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)
        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not confirmation:
            return apology("must provide Confirmation!!", 400)

        # Ensure password and Confirmation password are the same
        if password != confirmation:
            return apology("Your password is not match with the confirmation.Please try again")
        hash = generate_password_hash(password)

        # insert users into users table in database and tested the user is already exist
        try:
            db.execute("INSERT INTO users (username,hash) VALUES( ?, ?) ", username, hash)
            return redirect("/")
        except:
            return apology("The Username is already taken!")

    else:
        return render_template("register.html")

