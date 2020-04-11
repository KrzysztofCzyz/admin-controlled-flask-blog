from datetime import datetime
from blog_posts import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_header = db.relationship('PostHeader',
                               backref=db.backref('post', lazy=True, uselist=False), lazy=True, uselist=False)
    p_content = db.relationship('PostContent',
                                backref=db.backref('post', lazy=True, uselist=False), lazy=True, uselist=False)
    p_metadata = db.relationship('PostMetadata',
                                 backref=db.backref('post', lazy=True, uselist=False), lazy=True, uselist=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref=db.backref('author', lazy=True, uselist=False), lazy=True)


class PostHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    lead_graphic = db.Column(db.String(120), nullable=False)
    lead_text = db.Column(db.String(300), nullable=True)


class PostContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    text = db.Column(db.Text(), nullable=False)


class PostMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    views = db.Column(db.Integer, nullable=False, default=0)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
