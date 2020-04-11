from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_envvar('FLASK_APP_SETTINGS')
db = SQLAlchemy(app=app)

import blog_posts.routes
