from dynaconf import FlaskDynaconf

from flask import Flask

from shipay.extensions import db

from shipay.api import resources

def create_app() -> Flask:
    app = Flask('shipay')

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app: Flask):
    FlaskDynaconf(app)
    db.init_app(app)

def register_blueprints(app: Flask):
    app.register_blueprint(resources.bp)
