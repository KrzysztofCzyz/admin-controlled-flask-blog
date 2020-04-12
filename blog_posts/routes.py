from blog_posts import app, db
import logging
from flask import render_template, redirect, url_for, flash
from blog_posts.forms import SignInForm, NewPostForm
from blog_posts.models import Post, PostContent, PostHeader, PostMetadata
from blog_posts.utils import get_post_headers, get_post_vm_by_id


@app.route('/')
@app.route('/home')
def home():
    post_vms = get_post_headers()
    return render_template('home.html', posts=post_vms, title='Home')


@app.route('/signin', methods=('POST', 'GET'))
@app.route('/login', methods=('POST', 'GET'))
def login():
    form = SignInForm()
    if form.validate_on_submit():
        pass
    return render_template('sign-in.html', title='Sign In', form=form)


@app.route('/post/<post_id>:int')
def article(post_id):
    post_vm = get_post_vm_by_id(post_id)
    return render_template('post.html', title=post_vm['title'], post=post_vm)


@app.route('/new-post', methods=('POST', 'GET'))
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():

        post = Post(author_id=1)
        db.session.add(post)
        db.session.commit()

        if len(form.content.data) > 260:
            lead_text = form.content.data[0:261]
        else:
            lead_text = form.content.data

        ph = PostHeader(post_id=post.id, title=form.title.data.title(), lead_graphic="pupper.jpeg",
                        lead_text=lead_text)
        pc = PostContent(post_id=post.id, text=form.content.data)
        pmd = PostMetadata(post_id=post.id, author_id=1)

        db.session.add(ph)
        db.session.add(pc)
        db.session.add(pmd)
        db.session.commit()

        flash('Post Created!', category='success')

        return redirect(url_for('home'))
    return render_template('post-editor.html', title='New Post', form=form, action='Create a Post')


@app.route('/reset')
def reset_password():
    pass
