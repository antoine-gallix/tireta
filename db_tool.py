import records
from tireta import app

db = records.Database(app.config['SQLALCHEMY_DATABASE_URI'])
rows = db.query('select * from note')
