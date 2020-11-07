from datetime import datetime, timedelta

class Assignment:
    def __init__(self, data_list):
        self.title       = data_list[0]
        self.description = data_list[1] 
        self.due_date    = datetime.strptime(data_list[2], "%b %d, %Y %H:%M %p")
        self.max_score   = data_list[3]
        self.upload_link = data_list[4]
        self.attachments = data_list[5]
    
    def has_passed(self):
        now = datetime.now()
        if now <= self.due_date:
            return False
        else:
            return True
