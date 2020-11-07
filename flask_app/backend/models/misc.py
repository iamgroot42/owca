from datetime import datetime, timedelta
from .user import User

class Announcement:
    def __init__(self, data_list):
        self.title       = data_list[0]
        self.description = data_list[1]
        self.timestamp   = datetime.strptime(data_list[2], "%b %d, %Y %H:%M %p")
        self.link        = data_list[3]
