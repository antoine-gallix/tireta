from tireta import create_app
from tireta.models import db, User, Note, Tag

from tests.db_utils import *
app = create_app()
print(app.url_map)
app.app_context().push()
s = db.session()

# -----------------------------------------------
from tireta.serializing import user_schema
u = s.query(User).first()
user_schema.dumps(u).data
