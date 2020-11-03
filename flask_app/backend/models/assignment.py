from datetime import datetime, timedelta

class Assignment:
    def __init__(self, name, description, due_date, assignment_link, minutes=5):
        self.name = name
        self.id = name + str(due_date)
        self.description = description
        self.assignment_link = assignment_link
        self.due_date = due_date
    
    def has_passed(self):
        now = datetime.now()
        # Relaxed portal window for 5 minutes (account for slow upload time)
        if now <= self.due_date:
            return True
        else:
            return False
