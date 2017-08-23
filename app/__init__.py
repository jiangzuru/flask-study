from flask import Flask 
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def stapp(config_name):
	app = Flask(__name__)

	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)

	from .login import login as login_blueprint
	app.register_blueprint(login_blueprint)


	return app