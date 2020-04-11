from blog_posts import app, db
from flask import render_template, redirect, url_for, flash
from blog_posts.forms import SignInForm, NewPostForm
from blog_posts.models import Post, PostContent, PostHeader, PostMetadata

posts = [
    {
        'post-id': 1,
        'title': 'First Post',
        'lead': 'Content lead',
        'content': 'First post content',
        'contentId': 1,
        'lastUpdated': 180,
        'authorId': 1,
        'leadImage': 'pupper.jpeg'
    },
    {
        'post-id': 2,
        'title': 'Sec Post',
        'lead': 'Content lead',
        'content': 'Second post content',
        'contentId': 1,
        'lastUpdated': 180,
        'authorId': 1,
        'leadImage': 'firefox-logo.png'
    }
]

authors = [
    {
        'id': 1,
        'first-name': 'Janusz',
        'last-name': 'Pawlacz'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/signin', methods=('POST', 'GET'))
@app.route('/login', methods=('POST', 'GET'))
def login():
    form = SignInForm()
    if form.validate_on_submit():
        pass
    return render_template('sign-in.html', title='Sign In', form=form)


@app.route('/new-post', methods=('POST', 'GET'))
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        flash('Post Created!', category='success')
        post = Post(author_id=1)
        post.post_header = PostHeader(title=form.title, lead_graphic=form.leadimg)
        post.post_content = PostContent(text=form.content)
        post.post_metadata = PostMetadata()
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('post-editor.html', title='New Post', form=form, action='Create a Post')


@app.route('/reset')
def reset_password():
    pass
