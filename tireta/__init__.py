from .application import create_app
import logging
from .config import logging_config

# setup logging
logging.config.dictConfig(logging_config)
logging.info('\n' * 10)
