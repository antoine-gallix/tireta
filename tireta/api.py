from .models import Note, User, Tag, db
import logging
from flask_restful import Resource, Api
from .serializing import user_schema, user_collection_schema
from pdb import set_trace as bp

api = Api()
session = db.session


class UserCollection(Resource):

    def get(self):
        users = session.query(User).all()
        users_json = user_collection_schema.dumps(users).data
        return users_json

api.add_resource(UserCollection, '/api/users')


class UserSingle(Resource):

    def get(self, user_id):
        user = session.query(User).filter_by(id=user_id).one()
        user_json = user_schema.dumps(user).data
        return user_json

api.add_resource(UserSingle, '/api/users/<int:user_id>')
