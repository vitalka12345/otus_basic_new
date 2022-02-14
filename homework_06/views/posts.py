import logging

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

from models import db, Posts

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/", endpoint="list")
def list_posts():
    posts = Posts.query.order_by(Posts.id).all()
    return render_template(
        "posts/list.html",
        posts=posts,
    )


def get_post_userid_from_form():
    post_userid = request.form.get("post-user-id")
    if userid := (post_userid and post_userid.strip()):
        print(userid)
        return userid

    raise BadRequest("field post-user-id is required!")


def get_post_title_from_form():
    post_title = request.form.get("post-title")
    if title := (post_title and post_title.strip()):
        print(title)
        return title

    raise BadRequest("field post-title is required!")


def get_post_body_from_form():
    post_body = request.form.get("post-body")
    if body := (post_body and post_body.strip()):
        print(body)
        return body

    raise BadRequest("field post-body is required!")


def save_post(post_userid, post_title, post_body):
    try:
        db.session.commit()
    except IntegrityError as ex:
        logging.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save post {post_userid, post_title, post_body}, "
                         f"probably userid, title, body is not unique")
    except DatabaseError:
        db.session.rollback()
        logging.exception("got db error!")
        raise InternalServerError(f"could not save post with userid, title, body "
                                  f"{post_userid, post_title, post_body}!")


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_post():
    if request.method == "GET":
        return render_template("posts/add.html")

    post_userid = get_post_userid_from_form()
    post_title = get_post_title_from_form()
    post_body = get_post_body_from_form()
    post = Posts(userid=post_userid, title=post_title, body=post_body)
    db.session.add(post)
    save_post(post_userid, post_title, post_body)
    return redirect(url_for("posts_app.list"))
