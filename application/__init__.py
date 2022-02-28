from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] + f"postgres:/{os.environ.get('FLASK_DB_PASSWORD')}@localhost:5432/enrollment"

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes
