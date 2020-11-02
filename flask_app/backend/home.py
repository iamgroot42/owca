from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from backend.auth import login_required
from backend.db import get_db

from tinydb import Query
from .models.user import User

bp = Blueprint("home", __name__)


@bp.route("/")
@login_required
def index():
    """Home view"""
    """Show all upcoming deadlines and list courses."""
    # db = get_db()

    # Get current user's courses
    courses = g.user.get_courses()
    # Get deadlines for those courses
    deadlines = g.user.get_assignments()
    # Pick only the ones that are due 
    deadlines = [x for x in deadlines if not x.has_passed()]
    # Get them ready with tags, sort by due date
    return render_template("home/index.html", deadlines=deadlines, courses=courses)


# @bp.route("/create", methods=("GET", "POST"))
# @login_required
# def create():
#     """Create a new post for the current user."""
#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None

#         if not title:
#             error = "Title is required."

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
#                 (title, body, g.user["id"]),
#             )
#             db.commit()
#             return redirect(url_for("blog.index"))

#     return render_template("blog/create.html")


# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# @login_required
# def update(id):
#     """Update a post if the current user is the author."""
#     post = get_post(id)

#     if request.method == "POST":
#         title = request.form["title"]
#         body = request.form["body"]
#         error = None

#         if not title:
#             error = "Title is required."

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
#             )
#             db.commit()
#             return redirect(url_for("blog.index"))

#     return render_template("blog/update.html", post=post)


# @bp.route("/<int:id>/delete", methods=("POST",))
# @login_required
# def delete(id):
#     """Delete a post.

#     Ensures that the post exists and that the logged in user is the
#     author of the post.
#     """
#     get_post(id)
#     db = get_db()
#     db.execute("DELETE FROM post WHERE id = ?", (id,))
#     db.commit()
#     return redirect(url_for("blog.index"))