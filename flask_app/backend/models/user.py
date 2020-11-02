class User:
    def __init__(self, username, courses=[], submissions=[]):
        self.username = username
        self.courses  = courses
        self.submissions = submissions

    def get_courses(self):
        return self.courses

    def drop_course(self, course_id):
        try:
            self.courses.remove(course_id)
            return True
        except ValueError:
            return False
    
    def add_course(self, course):
        self.courses.append(course)

    def get_assignments(self):
        assignments = []
        for course in self.courses:
            for assignment in course.get_assignments():
                assignments.append(assignment)
        return assignments