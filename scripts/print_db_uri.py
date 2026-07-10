import os
import sys

# ensure project root is on sys.path so imports work when run from scripts/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

os.environ['DB_USE_SQLITE'] = '1'
from app import app

print(app.config['SQLALCHEMY_DATABASE_URI'])
