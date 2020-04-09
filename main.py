from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'post-id': 1,
        'name': 'First Post',
        'lead': 'Content lead',
        'content': 'First post content',
        'content-id': 1,
        'last-updated': 180,
        'author-id': 1
    },
    {
        'post-id': 3,
        'name': 'Sec Post',
        'lead': 'Content lead',
        'content': 'Second post content',
        'content-id': 1,
        'last-updated': 180,
        'author-id': 1
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
    return render_template('layout.html')
