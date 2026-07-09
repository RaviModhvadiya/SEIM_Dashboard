from flask import Blueprint, render_template

logs = Blueprint("logs", __name__)

@logs.route("/logs")
def logs_page():
    return render_template("logs/logs.html")