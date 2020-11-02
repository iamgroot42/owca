from datetime import datetime, timedelta

class Assignment:
    def __init__(self, name, description, due_date, minutes=5):
        self.name = name
        self.id = name + str(due_date)
        self.description = description
        self.due_date = due_date
        self.buffer = timedelta(minutes=minutes)
    
    def has_passed(self):
        now = datetime.now()
        # Relaxed portal window for 5 minutes (account for slow upload time)
        if now <= self.due_date + self.buffer:
            return True
        else:
            return False

    def change_due_date(self, new_date):
        self.due_date = new_date
