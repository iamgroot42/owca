class User:
    def __init__(self, id, courses):
        self.id = id
        self.courses  = courses

    def get_courses(self):
        return self.courses
