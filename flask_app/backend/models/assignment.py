from datetime import datetime, timedelta

class Assignment:
    def __init__(self, name, description, due_date, assignment_link):
        self.name = name
        # self.id = name + str(due_date)
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d, %H:%M:%S")
        self.assignment_link = assignment_link
    
    def has_passed(self):
        now = datetime.now()
        print(now)
        print(self.due_date)
        if now <= self.due_date:
            return False
        else:
            return True
