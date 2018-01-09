from .models import Note, User, Tag, db
import logging
from flask_restful import Resource, Api
from flask import request
from .serializing import user_schema, user_collection_schema
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


class UserResource(Resource):

    def post(self):
        user = user_schema.load(request.json).data
        db.session.add(user)
        db.session.commit()
        feedback = user_schema.dumps(user).data
        return feedback, 201

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
