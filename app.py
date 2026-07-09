from flask import Flask

from config import Config

from models import db
from models import login_manager

from models.user import User
from models.log import Log

from routes.home import home
from routes.auth import auth
from routes.dashboard import dashboard
from routes.upload import upload

from models.log_entry import LogEntry

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(home)

app.register_blueprint(auth)

app.register_blueprint(dashboard)

app.register_blueprint(upload)

if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(debug=True)