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

    coursedb = get_db()[0]

    # Get current user's course IDs
    courses = g.user.get_courses()

    # Get courses from course DB
    deadlines = []
    for id in courses:
        act_course = coursedb.get(id)
        deadlines += act_course.get_assignments()

    # Pick only the ones that are due 
    deadlines = [x for x in deadlines if not x.has_passed()]
    # Sort by due date
    deadlines = sorted(deadlines,
        key=lambda x: x.due_date,
        reverse=True)
    days_left = get_timer_content([x.due_date for x in deadlines])
    due_today = [((x.due_date - datetime.now()).days == 0) for x in deadlines]
    # Get them ready with tags, sort by due date
    today = 1 + (datetime.today().weekday() + 1)%7

    return render_template("home/index.html",
                    deadlines=deadlines,
                    courses=courses,
                    badges=days_left,
                    due_today=due_today,
                    calendar_link=g.user.calendar_link,
                    today=today)
