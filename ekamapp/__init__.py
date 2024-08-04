from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
import logging
from logging.handlers import RotatingFileHandler

app=Flask(__name__)

#Loading Environment Variables
environment=os.getenv('FLASK_ENV', 'development')
config=Config(environment=environment)
app.config['SECRET_KEY']=config.get('app.secret_key')
app.config['SQLALCHEMY_DATABASE_URI']=config.get('database.uri')
app.config['DEBUG']=config.get('app.debug')
db=SQLAlchemy(app)

from ekamapp.user.routes import users
app.register_blueprint(users)
# Logging Configuration
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/ekamapp.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('EkamApp startup')
