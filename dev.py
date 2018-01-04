from tireta.models import User, Note, Tag
from tireta import app, api, db
from tests.db_utils import *


app.app_context().push()
print(current_app.url_map)
s = db.session()

# -----------------------------------------------
