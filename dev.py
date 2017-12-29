from tireta.models import User, Note, Tag
from tireta import db, create_app
app = create_app()
app.app_context().push()

# -----------------------------------------------
