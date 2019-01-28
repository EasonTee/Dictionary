from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '\t\xa9\x7f\x86mA#\xa0\x8a\x81I\x7f<\x7f;\x11\xe2v*\xc1}0T\x92'

from app import routes
