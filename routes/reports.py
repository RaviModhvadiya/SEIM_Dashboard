from flask import Blueprint, render_template

reports = Blueprint("reports", __name__)

@reports.route("/reports")
def reports_page():
    return render_template("reports/reports.html")