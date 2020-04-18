#!/usr/bin/python3

from blog_posts import db
from blog_posts.models import *
from admin_backend.models import *

db.create_all()

user = User(id='random', email='jan@jan.pl', password='sample')

db.session.add(user)
db.session.commit()

author = Author(name='Jan', surname='Kowalski')

db.session.add(author)
db.session.commit()

post = Post(author_id=1)
db.session.add(post)
db.session.commit()

post_header = PostHeader(post_id=1, title='Sample title', lead_graphic='pupper.jpeg',
                lead_text='Sample lead text')

db.session.add(post_header)
db.session.commit()

post_content = PostContent(post_id=1, text='Sample Post Content')
post_metadata = PostMetadata(author_id=1, post_id=1, views=20)

db.session.add(post_content)
db.session.add(post_metadata)
db.session.commit()


