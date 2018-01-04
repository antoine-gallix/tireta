from pdb import set_trace as bp
import flask
from .models import db
# from .api import api, create_apis
from .config import DevConfig, logging_config
import logging
import logging.config

# setup logging
logging.config.dictConfig(logging_config)
logging.info('\n' * 10)

# setup app
logging.info('setting up app')
app = flask.Flask(__name__)
app.config.from_object(DevConfig)

# setup extensions
logging.info('setting up db')
db.init_app(app)
logging.info('setting up api')
# api.init_app(app=app, flask_sqlalchemy_db=db)
# create_apis(app, api)
