
from Artisan import db,login_manager,bcrypt
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Define Model
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String,nullable=False)

    def __repr__(self):
        return f'User{self.username}'

    
    def verify_password(self, attempted_password):
        return check_password_hash(self.password, attempted_password)

#Create BLog Post
class Posts(db.Model,UserMixin):
    post_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    post_date = db.Column(db.DateTime,default=datetime.utcnow)