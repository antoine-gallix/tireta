from pdb import set_trace as bp
import flask
from .models import db
from .api import api
from .config import DevConfig, TestConfig
import logging
import logging.config


def create_app(config='dev'):
    # setup app
    logging.info('creating app with \'{}\' config'.format(config))
    app = flask.Flask(__name__)
    if config == 'dev':
        config_object = DevConfig
    if config == 'test':
        config_object = TestConfig
    app.config.from_object(config_object)
    logging.info('db uri : {}'.format(config_object.SQLALCHEMY_DATABASE_URI))

    # setup extensions
    db.init_app(app)
    api.init_app(app)

    return app
