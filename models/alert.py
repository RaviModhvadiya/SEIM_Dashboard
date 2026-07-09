from models import db


class Alert(db.Model):

    __tablename__ = "alerts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    log_entry_id = db.Column(
        db.Integer,
        db.ForeignKey("log_entries.id"),
        nullable=False
    )

    alert_type = db.Column(
        db.String(100)
    )

    severity = db.Column(
        db.String(20)
    )

    description = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Open"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )