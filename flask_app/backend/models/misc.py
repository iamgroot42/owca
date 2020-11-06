from datetime import datetime, timedelta
from .user import User

class Announcement:
    def __init__(self, title, text, timestamp=None):
        self.title = title
        self.text = text
        if timestamp is None: self.timestamp = datetime.now()

class TA(User):
    def __init__(self, user_id):
        super(TA, self).__init__(user_id)
    
    def add_office_hours(self, office_hours, office_link):
        self.office_hours = office_hours
        self.office_link = office_link
        
    def get_office_hours(self):
        return (self.office_hours,  self.office_link)


class Instructor(TA):
    def __init__(self, user_id, courses):
        super(Instructor, self).__init__(user_id)
        self.courses = courses


class Session:
    def __init__(self, year, term):
        self.year = year
        self.term = term
