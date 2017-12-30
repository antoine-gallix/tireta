from pdb import set_trace as bp
import flask
import flask_restless
import flask_sqlalchemy
from .config import config, logging_config
import logging
import logging.config

# setup logging
logging.config.dictConfig(logging_config)

api = flask_restless.APIManager()
db = flask_sqlalchemy.SQLAlchemy()


def create_app(config_name='default'):
    # setup app
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])

    # setup extensions
    db.init_app(app)
    api.init_app(app=app, flask_sqlalchemy_db=db)

    # setup API
    from . import models
    api.create_api(models.Note, methods=['GET', 'POST', 'DELETE'],
                   preprocessors={'POST': [models.note_post_preprocessor]},
                   postprocessors={'POST': [models.note_post_postprocessor]},
                   )
    api.create_api(models.User, methods=['GET', 'POST', 'DELETE'])
    api.create_api(models.Tag, methods=['GET'])

    return app
