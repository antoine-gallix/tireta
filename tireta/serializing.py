from marshmallow_sqlalchemy import ModelSchema
from .models import User, Note, Tag


class UserSchema(ModelSchema):

    class Meta:
        model = User

user_schema = UserSchema()
user_collection_schema = UserSchema(many=True)
