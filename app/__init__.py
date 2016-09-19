from flask import Flask
from config import config
import os
from flask.ext.sqlalchemy import SQLAlchemy



from app import views


basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
app = Flask(__name__)
config_name='development'
app.config.from_object(app.config.from_object(config[config_name]))
config[config_name].init_app(app)
# Set up extensions
db.init_app(app)