import os
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','sqlite:///spentrack.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
