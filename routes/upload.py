from cmath import log
import os

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import current_app

from flask_login import login_required
from flask_login import current_user

from werkzeug.utils import secure_filename

from models import db
from models.log import Log
from services.log_parser import parse_csv

upload = Blueprint(
    "upload",
    __name__,
    url_prefix="/upload"
)

ALLOWED_EXTENSIONS = {"csv"}


def allowed_file(filename):

    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@upload.route("/", methods=["GET", "POST"])
@login_required
def upload_log():

    if request.method == "POST":

        if "logfile" not in request.files:

            flash("No file selected.", "danger")

            return redirect(request.url)

        file = request.files["logfile"]

        if file.filename == "":

            flash("Please choose a file.", "warning")

            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            upload_folder = current_app.config["UPLOAD_FOLDER"]

            os.makedirs(upload_folder, exist_ok=True)

            filepath = os.path.join(upload_folder, filename)

            file.save(filepath)

            log = Log(

                filename=filename,

                log_type=request.form.get("log_type"),

                uploaded_by=current_user.id

            )

            db.session.add(log)

            db.session.commit()

            rows = parse_csv(filepath, log.id)

            flash(
                f"{rows} log entries imported successfully!",
                "success"
                )

            flash(
                "Log uploaded successfully!",
                "success"
            )

            return redirect(url_for("upload.upload_log"))

        flash(
            "Only CSV files are allowed.",
            "danger"
        )

    return render_template("upload/upload.html")