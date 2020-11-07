from backend.models.course import Course
from backend.models.assignment import Assignment
from backend.models.misc import Announcement
from backend.models.user import User


def make_course_objects(courses, assignments, announcements):
    course_map = {}
    # Make course objects
    for course in courses.values:
        id   = course[0]
        course_map[id] = Course(course[1:])
    
    # Iterate through announcements, add to courses
    for announcement in announcements.values:
        courseid = announcement[1]
        annct = Announcement(announcement[2:])
        course_map[courseid].add_announcement(annct)
    
    # Iterate through assignments, add to courses
    for assignment in assignments.values:
        courseid = assignment[1]
        assgt = Assignment(assignment[2:])
        course_map[courseid].add_assignment(assgt)
    
    return course_map


def make_user_objects(users):
    user_map = {}
    for user in users.values:
        userid = user[0]
        user_map[userid] = User(user)
    return user_map
