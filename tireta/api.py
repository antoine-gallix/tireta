from .models import Note, User, Tag, db
import logging
from flask_restful import Resource, Api
from flask import request
from .serializing import user_schema, user_collection_schema, note_schema, note_collection_schema, tag_schema, tag_collection_schema
from pdb import set_trace as bp
from sqlalchemy.orm.exc import NoResultFound
import json

session = db.session

errors = {
    # catch error coming from sqlalchemy when resource does not exist
    'NoResultFound': {
        'message': "The requested resource does not exist",
        'status': 404,
    },
}

api = Api(errors=errors)


# ---------------------GENERIC COMPONENTS---------------------

class Get_One_Or_All:
    """Generic mixin class that provides getting a single item or a collection
    """

    def get(self, item_id=None, **kwargs):
        if item_id:
            return self.get_one(item_id, **kwargs)
        else:
            return self.get_many(**kwargs)

    def get_one(self, item_id, **kwargs):
        item = session.query(self.model).filter_by(id=item_id).one()
        item_json = self.item_schema.dumps(item).data
        return item_json

    def get_many(self, **kwargs):
        items = session.query(self.model).all()
        items_json = self.item_collection_schema.dumps(items).data
        return items_json


# -------------------USER----------------------------


class UserResource(Resource, Get_One_Or_All):

    # class attribute to use for the generic mixins
    model = User
    item_schema = user_schema
    item_collection_schema = user_collection_schema

    def post(self):
        user = user_schema.load(request.json).data
        db.session.add(user)
        db.session.commit()
        feedback = user_schema.dumps(user).data
        return feedback, 201

    def delete(self, user_id=None):
        if user_id is None:
            return 'deletion works only on single user', 403
        try:
            user = session.query(User).filter_by(id=user_id).one()
            db.session.delete(user)
            db.session.commit()
            return 'user deleted', 204
        except NoResultFound:
            return 'user does not exist', 404

    def get(self, user_id=None):
        """get must be defined in this class to be recognized by RestFull extension
        """

        return super().get(item_id=user_id)

api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')


# ---------------------NOTE--------------------------


class NoteResource(Resource, Get_One_Or_All):

    # class attribute to use for the generic mixins
    model = Note
    item_schema = note_schema
    item_collection_schema = note_collection_schema

    def post(self, user_id=None):
        payload = request.json
        # i'm still not sure of deserializing nested models
        # so for now I pop them from payload and do it by hand
        if user_id is None:
            user_id = payload.pop('user_id')
        tag_names = payload.pop('tags', [])

        note = note_schema.load(payload).data

        # get user from database
        user = session.query(User).filter_by(id=user_id).one()
        note.user = user

        # create tags
        if tag_names:
            tags = [Tag(name=name) for name in tag_names]
        note.tags = tags
        db.session.add(note)
        db.session.commit()
        feedback = note_schema.dumps(note).data
        return feedback, 201

    def delete(self, note_id=None):
        if note_id is None:
            return 'deletion works only on single note', 403
        try:
            note = session.query(Note).filter_by(id=note_id).one()
            db.session.delete(note)
            db.session.commit()
            return 'note deleted', 204
        except NoResultFound:
            return 'note does not exist', 404

    def get(self, user_id=None, note_id=None):
        """get must be defined in this class to be recognized by RestFull extension
        """
        return super().get(item_id=note_id, user_id=user_id)

api.add_resource(NoteResource,
                 '/api/notes',
                 '/api/notes/<int:note_id>',
                 '/api/users/<int:user_id>/notes',
                 '/api/users/<int:user_id>/notes/<int:note_id>',
                 )


# ---------------------TAG---------------------


class TagResource(Resource, Get_One_Or_All):

    # class attribute to use for the generic mixins
    model = Tag
    item_schema = tag_schema
    item_collection_schema = tag_collection_schema

    def post(self):
        tag = tag_schema.load(request.json).data
        db.session.add(tag)
        db.session.commit()
        feedback = tag_schema.dumps(tag).data
        return feedback, 201

    def get(self, tag_id=None):
        """get must be defined in this class to be recognized by RestFull extension
        """
        return super().get(item_id=tag_id)

api.add_resource(TagResource, '/api/tags', '/api/tags/<int:tag_id>')
