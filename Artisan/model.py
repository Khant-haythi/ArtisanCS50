
from Artisan import db

#Define Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String,nullable=False)

    def __repr__(self):
        return f'User{self.username}'

