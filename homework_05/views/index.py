from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequest, NotFound

index_app = Blueprint("index_app", __name__)


@index_app.route("/")
def index():
    return render_template("others/index.html")


@index_app.route("/about/")
def about():
    return render_template("others/about.html")
