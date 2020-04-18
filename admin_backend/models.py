from flask_login import UserMixin
from blog_posts import db


# TODO - PASSWORDS!!

class User(db.Model, UserMixin):
    id = db.Column(db.Unicode(100), primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
