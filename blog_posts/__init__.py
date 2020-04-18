from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from flask_login import LoginManager

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config.from_envvar('FLASK_APP_SETTINGS')
db = SQLAlchemy(app=app)
login_manager = LoginManager()

from admin_backend.utils import load_user

login_manager.user_loader(load_user)
login_manager.init_app(app)
login_manager.login_message_category = "info"
login_manager.login_view = 'login'

import blog_posts.routes




