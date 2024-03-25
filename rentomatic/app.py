"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
"""
from flask import Flask
from rentomatic.rest import room
from rentomatic.flask_settings import DevelopmentConfig


def create_app(config_object=DevelopmentConfig) -> Flask:
    """
    This function creates the Flask app taken the config object as an argument.
    In addition, we add the room's endpoints to be exposed the URLs defined in.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(room.blueprint)
    return app
