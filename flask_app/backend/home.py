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
from .models.assignment import Assignment
from .models.course import Course
from datetime import datetime

bp = Blueprint("home", __name__)

def get_timer_content(dates):
    content = []
    nowtime = datetime.now()
    for d in dates:
        diff = (d - nowtime)
        if diff.days > 0:
            suffix = "Days" if diff.days > 1 else "Day"
            content.append("%d %s" % (diff.days, suffix))
        elif diff.seconds > 3600:
            suffix = "Hours" if (diff.seconds // 3600) > 1 else "Hour"
            content.append("%d %s" % (diff.seconds // 3600, suffix))
        else:
            suffix = "Minutes" if (diff.seconds // 60) > 1 else "Minute"
            content.append("%d %s" % (diff.seconds // 60, suffix))
    return content

@bp.route("/")
@login_required
def index():
    """Home view"""
    """Show all upcoming deadlines and list courses."""

    coursedb = get_db()[1]

    # Get current user's course IDs
    courses = g.user.get_courses()
    print(courses)

    # Get courses from course DB
    deadlines = []
    for course in courses:
        act_course = coursedb.search(Query().id == course)[0]["assignments"]
        for ccc in act_course:
            print(ccc)
            deadlines.append(Assignment(**ccc))
    # Pick only the ones that are due 
    deadlines = [x for x in deadlines if not x.has_passed()]
    # Sort by due date
    deadlines = sorted(deadlines, key=lambda x: x.due_date)
    days_left = get_timer_content([x.due_date for x in deadlines])
    due_today = [((x.due_date - datetime.now()).days == 0) for x in deadlines]
    # Get them ready with tags, sort by due date
    today = 1 + (datetime.today().weekday() + 1)%7
    return render_template("home/index.html",
                    deadlines=deadlines,
                    courses=courses,
                    badges=days_left,
                    due_today=due_today,
                    today=today)


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