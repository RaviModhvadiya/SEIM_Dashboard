from models import db


class LogEntry(db.Model):

    __tablename__ = "log_entries"

    id = db.Column(db.Integer, primary_key=True)

    log_id = db.Column(
        db.Integer,
        db.ForeignKey("logs.id"),
        nullable=False
    )

    event_time = db.Column(db.DateTime)

    event_level = db.Column(db.String(50))

    source = db.Column(db.String(100))

    message = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )