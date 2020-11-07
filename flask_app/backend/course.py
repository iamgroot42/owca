
from flask import Blueprint
from flask import flash
from flask import render_template
from flask import g

from backend.auth import login_required

bp = Blueprint("course", __name__)


@bp.route("/<int:id>")
@login_required
def index(id):
    """Update a post if the current user is the author."""

    return render_template("course/index.html", course=None)
