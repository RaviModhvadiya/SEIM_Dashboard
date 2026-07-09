from flask import Blueprint, render_template
from flask_login import login_required

from models.user import User
from models.log import Log
from models.log_entry import LogEntry
from models.alert import Alert

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    total_users = User.query.count()
    total_logs = Log.query.count()
    total_log_entries = LogEntry.query.count()
    total_alerts = Alert.query.count()
    critical_alerts = Alert.query.filter_by(severity="Critical").count()

    return render_template(
        "dashboard/index.html",
        total_users=total_users,
        total_logs=total_logs,
        total_log_entries=total_log_entries,
        total_alerts=total_alerts,
        critical_alerts=critical_alerts
    )