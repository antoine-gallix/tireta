from tireta.models import User, Note, Tag
from tireta import db, create_app
from tests.db_utils import *
from pdb import set_trace as bp
from flask import current_app


app = create_app()
app.app_context().push()
print(current_app.url_map)
# -----------------------------------------------
