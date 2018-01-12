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


# -------------------USER----------------------------


class UserResource(Resource):

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
        if user_id:
            return self.get_one(user_id)
        else:
            return self.get_many()

    def get_one(self, user_id):
        user = session.query(User).filter_by(id=user_id).one()
        user_json = user_schema.dumps(user).data
        return user_json

    def get_many(self):
        users = session.query(User).all()
        users_json = user_collection_schema.dumps(users).data
        return users_json

api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')


# ---------------------NOTE--------------------------


class NoteResource(Resource):

    def post(self, user_id=None):
        if user_id is None:
            user_id = request.json['user_id']
        note = note_schema.load(request.json).data
        user = session.query(User).filter_by(id=user_id).one()
        note.user = user
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

    def get(self, note_id=None):
        if note_id:
            return self.get_one(note_id)
        else:
            return self.get_many()

    def get_one(self, note_id):
        note = session.query(Note).filter_by(id=note_id).one()
        note_json = note_schema.dumps(note).data
        return note_json

    def get_many(self):
        notes = session.query(Note).all()
        notes_json = note_collection_schema.dumps(notes).data
        return notes_json


api.add_resource(NoteResource,
                 '/api/notes',
                 '/api/notes/<int:note_id>',
                 '/api/users/<int:user_id>/notes',
                 '/api/users/<int:user_id>/notes/<int:note_id>',
                 )


# ---------------------TAG---------------------


class TagResource(Resource):

    def post(self):
        tag = tag_schema.load(request.json).data
        db.session.add(tag)
        db.session.commit()
        feedback = tag_schema.dumps(tag).data
        return feedback, 201

    def get(self, tag_id=None):
        if tag_id:
            return self.get_one(tag_id)
        else:
            return self.get_many()

    def get_one(self, tag_id):
        tag = session.query(Tag).filter_by(id=tag_id).one()
        tag_json = tag_schema.dumps(tag).data
        return tag_json

    def get_many(self):
        tags = session.query(Tag).all()
        tags_json = tag_collection_schema.dumps(tags).data
        return tags_json

api.add_resource(TagResource, '/api/tags', '/api/tags/<int:tag_id>')
