from flask import Flask, render_template, redirect, url_for
from forms import SignInForm, NewPostForm

app = Flask(__name__)
app.config.from_envvar('FLASK_APP_SETTINGS')

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
        return redirect(url_for('home'))
    return render_template('post-editor.html', title='New Post', form=form, action='Create a Post')


@app.route('/reset')
def reset_password():
    pass
