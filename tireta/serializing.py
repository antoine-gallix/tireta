from marshmallow_sqlalchemy import ModelSchema
from .models import User, Note, Tag, db


class UserSchema(ModelSchema):

    class Meta:
        model = User
        sqla_session = db.session

user_schema = UserSchema()
user_collection_schema = UserSchema(many=True)
