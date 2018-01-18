from pdb import set_trace as bp
import flask
from .models import db
from .api import api
from .config import config_map
import logging
import logging.config


def create_app(config_key='dev'):
    logging.info('------CREATING APPLICATION------')
    # setup app
    logging.info('config : \'{}\' '.format(config_key))
    app = flask.Flask(__name__)
    config = config_map[config_key]
    app.config.from_object(config)
    logging.info('db uri : {}'.format(config.SQLALCHEMY_DATABASE_URI))
    logging.info('debug : {}'.format(config.DEBUG))

    # setup extensions
    db.init_app(app)
    api.init_app(app)

    return app
