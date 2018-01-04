from flask_restless import APIManager
from .models import Note, User, Tag
import logging

api = APIManager()


def note_post_preprocessor(data=None, **kw):
    logging.debug(data)
    pass


def note_post_postprocessor(result=None, **kw):
    logging.debug(result)
    pass


def create_apis(app, api):
    api.create_api(
        Note,
        app=app,
        methods=['GET', 'POST', 'DELETE'],
        preprocessors={
            'POST': [note_post_preprocessor]},
        postprocessors={
            'POST': [note_post_postprocessor]},
    )
    api.create_api(
        User,
        app=app,
        methods=['GET', 'POST', 'DELETE'])
    api.create_api(
        Tag,
        app=app,
        methods=['GET'])
