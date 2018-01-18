"""test client library againse a live running server
"""

from tireta_client.api_client import send_note, create_user
from pytest import mark
from urllib.parse import urlparse
from .db_utils import add_user, list_db
from pdb import set_trace as bp
import logging


pytestmark = mark.usefixtures('running_server')


def test_post_note(note_file_with_tags):
    logging.debug('starting server test')
    user = create_user('jean_louis')
    note = send_note(str(note_file_with_tags), user['id'])
