from datetime import datetime

class Submission:
    def __init__(self):
        self.submission_timestamp = None
        self.files = []

    def upload(self, user_id, content):
        self.user_id = user_id
        self.files.append(content)

    def submitted(self):
        self.submission_timestamp = datetime.now()
