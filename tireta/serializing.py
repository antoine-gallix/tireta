from marshmallow_sqlalchemy import ModelSchema
from .models import User, Note, Tag, db


class UserSchema(ModelSchema):

    class Meta:
        model = User
        sqla_session = db.session

user_schema = UserSchema()
user_collection_schema = UserSchema(many=True)


class NoteSchema(ModelSchema):

    class Meta:
        model = Note
        sqla_session = db.session

note_schema = NoteSchema()
note_collection_schema = NoteSchema(many=True)


class TagSchema(ModelSchema):

    class Meta:
        model = Tag
        sqla_session = db.session

tag_schema = TagSchema()
tag_collection_schema = TagSchema(many=True)
