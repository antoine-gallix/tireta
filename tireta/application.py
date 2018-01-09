from pdb import set_trace as bp
import flask
from .models import db
from .api import api
from .config import config_map
import logging
import logging.config


def create_app(config_key='dev'):
    # setup app
    logging.info('creating app with \'{}\' config'.format(config_key))
    app = flask.Flask(__name__)
    app.config.from_object(config_map[config_key])
    logging.info('db uri : {}'.format(
        config_map[config_key].SQLALCHEMY_DATABASE_URI))

    # setup extensions
    db.init_app(app)
    api.init_app(app)

    return app
