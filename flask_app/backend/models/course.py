class Course:
    def __init__(self, data_list):
        self.course_code = data_list[0]
        self.instructor  = data_list[1]
        self.tas         = data_list[2].split(",")
        self.description = data_list[3]
        self.meeting_lnk = data_list[4]
        self.schedule    = data_list[5]
        self.syllabus    = data_list[6]
        self.course_site = data_list[7]
        self.instr_oh    = data_list[8]
        self.course_name = data_list[9]
        
        self.assignments = []
        self.annoucements = []
    
    def add_announcement(self, annoucement):
        self.annoucements.append(annoucement)
    
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    
    def get_assignments(self):
        return self.assignments
    
    def submit(self, assignment, submission):
        # If deadline has not passed, accept submission
        if assignment not in self.assignments:
            raise ValueError("Assignment does not exist!")
        
        if assignment.has_passed():
            return False
        else:
            # Redirect to Colab
            return True
