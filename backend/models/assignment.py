from datetime import datetime, timedelta
import math

class Assignment:
    def __init__(self, data_list, resource_attachments):
        self.title       = data_list[0]
        self.description = data_list[1] if data_list[1] != "" else ""
        print(data_list[2])
        self.due_date    = datetime.strptime(data_list[2].strip(), "%b %d, %Y %I:%M %p")
        print(self.due_date)
        self.max_score   = data_list[3] if data_list[3] != "" else ""
        self.upload_link = data_list[4]
        self.attachments = data_list[5] if type(data_list[5]) == str else ""
        self.resources   = resource_attachments
        
    def has_passed(self):
        now = datetime.now()
        if now <= self.due_date:
            return False
        else:
            return True
