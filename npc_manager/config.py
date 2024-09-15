import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MY_ENV_VAR = 'XY'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
