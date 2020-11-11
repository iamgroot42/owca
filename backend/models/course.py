class Course:
    def __init__(self, data_list):
        self.course_code = data_list[0]
        self.instructor  = data_list[1]
        self.tas         = data_list[2].split(",") if type(data_list[2]) == str else ""
        self.description = data_list[3] if type(data_list[3]) == str else ""
        self.meeting_lnk = data_list[4] if type(data_list[4]) == str else ""
        self.schedule    = data_list[5] if type(data_list[5]) == str else ""
        self.syllabus    = data_list[6] if type(data_list[6]) == str else ""
        self.course_site = data_list[7] if type(data_list[7]) == str else ""
        self.instr_oh    = data_list[8] if type(data_list[8]) == str else ""
        self.course_name = data_list[9]
        
        self.assignments = []
        self.annoucements = []
    
    def add_announcement(self, annoucement):
        self.annoucements.append(annoucement)
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    
    def get_assignments(self):
        return self.assignments
    
    def get_announcements(self):
        return self.annoucements
    
    def submit(self, assignment, submission):
        # If deadline has not passed, accept submission
        if assignment not in self.assignments:
            raise ValueError("Assignment does not exist!")
        
        if assignment.has_passed():
            return False
        else:
            # Redirect to Colab
            return True
