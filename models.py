from main import db
from datetime import datetime

# TODO fix data relationships as per https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_id = db.Column(db.Integer, db.ForeignKey('postheader.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('postcontent.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    metadata_id = db.Column(db.Integer, db.ForeignKey('postmetadata.id'), nullable=False)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref='author')


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
    last_updated = db.Column(db.Integer, nullable=True)
    views = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
