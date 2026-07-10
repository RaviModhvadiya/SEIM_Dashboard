import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    # Prefer MySQL when env vars provided, otherwise use a local SQLite file for dev/test
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    use_sqlite_flag = os.getenv("DB_USE_SQLITE", "").lower() in ("1", "true", "yes")

    if not use_sqlite_flag and db_host and db_name and db_user is not None:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
    else:
        sqlite_path = os.path.join(os.path.dirname(__file__), "database", "seim.db")
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{sqlite_path}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = "uploads"