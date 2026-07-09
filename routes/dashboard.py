from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user
from flask import Blueprint, render_template


dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)

dashboard = Blueprint(
    "dashboard",
    __name__
)

@dashboard.route("/dashboard")
def dashboard_home():

    return render_template(
        "dashboard/index.html"
    )

@dashboard.route("/")
@login_required
def home():

    return render_template(
        "dashboard/dashboard.html",
        user=current_user
    )