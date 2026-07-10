import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ['DB_USE_SQLITE'] = '1'
from app import app

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
