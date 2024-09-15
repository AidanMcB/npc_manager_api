from flask import Flask
from npc_manager.modules import hello, goodbye, cars, user, characters
from npc_manager.config import Config
from flask_migrate import Migrate
from npc_manager.database import db
from dotenv import load_dotenv
import os

# application factory 

def create_app():    
    app = Flask(__name__)        
    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )     
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    
    app.config.from_object(Config)
    
    # Database Initialization
    db.init_app(app)
    from npc_manager.models.user import User
    from npc_manager.models.car import Car
    migrate = Migrate(app, db)
    
    app.register_blueprint(hello.blueprint)
    app.register_blueprint(goodbye.blueprint)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(cars.blueprint)
    app.register_blueprint(characters.blueprint)
    
    return app