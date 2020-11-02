class Course:
    def __init__(self, id, instructor, session):
        self.id = id
        self.instructor = instructor
        self.tas = []
        self.session = session
        self.description = ""
        self.assignments = []
        self.submissions = {}
        self.meetings    = []
        self.annoucements = []
    
    def update_description(self, description):
        self.description = description
    
    def announce(self, annoucement):
        self.annoucements.append(annoucement)
    
    def add_ta(self, ta):
        self.tas.append(ta)

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
            # Will overwrite user's submission if exists
            submission.submitted()
            submissions = self.submissions.get(assignment.id, [])
            submissions.append(submission)
            self.submissions[assignment.id] = submissions
            return True
