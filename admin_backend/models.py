from flask_login import UserMixin
from blog_posts import db


class User(db.Model, UserMixin):
    id = db.Column(db.Unicode(100), primary_key=True)
