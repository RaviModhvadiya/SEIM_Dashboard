from flask import Blueprint, render_template

alerts = Blueprint("alerts", __name__)

@alerts.route("/alerts")
def alerts_page():
    return render_template("alerts/alerts.html")