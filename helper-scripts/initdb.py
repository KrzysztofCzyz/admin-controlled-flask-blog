#!/usr/bin/python3

from blog_posts import db
from blog_posts.models import *
from admin_backend.models import *

db.create_all()

x = Author(name='Jan', surname='Kowalski')

db.session.add(x)
db.session.commit()

post = Post(author_id=1)
db.session.add(post)
db.session.commit()

ph = PostHeader(post_id=1, title='Sample title', lead_graphic='pupper.jpeg',
                lead_text='Sample lead text')

db.session.add(ph)
db.session.commit()

pc = PostContent(post_id=1, text='Sample Post Content')
pmd = PostMetadata(author_id=1, post_id=1, views=20)

db.session.add(pc)
db.session.add(pmd)
db.session.commit()
