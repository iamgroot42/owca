class User:
    def __init__(self, username, courses=[], submissions=[]):
        self.username = username
        self.courses  = courses
        self.submissions = submissions

    def get_courses(self):
        return self.courses

    def get_assignments(self):
        assignments = []
        for course in self.courses:
            for assignment in course.get_assignments():
                assignments.append(assignment)
        return assignments