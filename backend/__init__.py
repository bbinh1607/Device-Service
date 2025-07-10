from flask import Flask
from backend.extensions import db, init_extensions
from backend.config import Config
from backend.controller import register_controllers
from backend.utils.converters.uuid_converter import UUIDConverter
from backend.entity import *  

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    init_extensions(app)
    
    app.url_map.converters['uuid'] = UUIDConverter

    with app.app_context():
        db.create_all()  # Tạo tất cả các bảng sau khi đã import entities
    
    # register_authentication(app)

    register_controllers(app)

    return app
