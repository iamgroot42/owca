
from flask import Blueprint
from flask import flash
from flask import render_template
from flask import g

from backend.auth import login_required

bp = Blueprint("course", __name__, url_prefix="/course")


@bp.route("/<int:id>")
@login_required
def index(id):

    # Get course object for this course
    course = g.db[0].get(id, None)
    error = None

    if course is None:
        error = "Incorrect course."
        
    if error is None:
        # Sort announcements
        annoucements = sorted(course.get_announcements(),
                        key=lambda x: x.timestamp,
                        reverse=True)
        # Sort assignments
        assignments = sorted(course.get_assignments(),
                        key=lambda x: x.due_date,
                        reverse=True)
    
        return render_template("course/index.html",
                            course=id,
                            class_link=course.meeting_lnk,
                            code=course.course_code,
                            name=course.course_name,
                            description=course.description,
                            schedule=course.schedule,
                            annoucements=annoucements,
                            syllabus=course.syllabus,
                            office_hours=course.instr_oh,
                            assignments=assignments)
    
    flash(error)
