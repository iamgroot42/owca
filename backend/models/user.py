class User:
    def __init__(self, data_list):
        self.alias         = data_list[0]
        self.name          = data_list[1]
        self.courses       = [int(x) for x in str(data_list[2]).split(",")]
        self.calendar_link = data_list[3]

    def get_courses(self):
        return self.courses
