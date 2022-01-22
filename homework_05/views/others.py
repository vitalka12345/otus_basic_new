from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound

others_app = Blueprint("others_app", __name__)


@others_app.route("/")
def other_index():
    return render_template("others/index.html")


@others_app.route("/about/")
def other_about():
    return render_template("others/about.html")
