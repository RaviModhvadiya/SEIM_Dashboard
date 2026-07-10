import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ['DB_USE_SQLITE'] = '1'
from app import app, db
with app.app_context():
    db.create_all()
    print('db created at', app.config['SQLALCHEMY_DATABASE_URI'])
