from flask import Blueprint, render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from werkzeug.security import generate_password_hash

from models import db
from models.user import User

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from werkzeug.security import check_password_hash

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_username = User.query.filter_by(
            username=username
        ).first()

        if existing_username:

            flash(
                "Username already exists.",
                "danger"
            )

            return redirect(url_for("auth.register"))

        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:

            flash(
                "Email already exists.",
                "danger"
            )

            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        user = User(

            full_name=full_name,

            username=username,

            email=email,

            password=hashed_password

        )

        db.session.add(user)

        db.session.commit()

        flash(
            "Registration Successful!",
            "success"
        )

        return redirect(url_for("home.index"))

    return render_template("auth/register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.home"))

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(
            username=username
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            flash(
                "Login Successful!",
                "success"
            )

            return redirect(
                url_for("dashboard.home")
            )

        flash(
            "Invalid Username or Password",
            "danger"
        )

    return render_template("auth/login.html")

@auth.route("/logout")
def logout():

    logout_user()

    flash(
        "Logged Out Successfully",
        "success"
    )

    return redirect(
        url_for("home.index")
    )