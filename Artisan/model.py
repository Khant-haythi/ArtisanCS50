from Artisan import db,login_manager,bcrypt
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Define Model
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    password = db.Column(db.String,nullable=False)
    cards = db.relationship('Cards',backref='owned_user',lazy=True)

    def __repr__(self):
        return f'User{self.username}'

    def verify_password(self, attempted_password):
        return check_password_hash(self.password, attempted_password)

class Cards(db.Model,UserMixin):
    card_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text)
    author = db.Column(db.String(255),nullable=False)
    created_date = db.Column(db.DateTime,default=datetime.utcnow)
    image_url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
