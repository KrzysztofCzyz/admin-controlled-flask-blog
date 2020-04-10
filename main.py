from flask import Flask, render_template, redirect, url_for
from forms import SignInForm

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
    return render_template('sign-in.html', title='Sign In', form=form)


@app.route('/new-post')
def new_post():
    return render_template('post-editor.html', title='New Post')
