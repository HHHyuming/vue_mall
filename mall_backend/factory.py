from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_migrate import MigrateCommand

from config import USE_CONFIG
from models import db
from models.User import *
from api import api
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    app.config.from_object(USE_CONFIG)

    # 初始化DB
    Migrate(app, db)
    db.init_app(app)
    # 初始化API
    api.init_app(app)

    # 同源策略
    CORS(app,  resources={r"/*": {"origins": "*"}})

    # script
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    return manager
