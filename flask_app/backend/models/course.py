class Course:
    def __init__(self, id, instructor, session, description, tas):
        self.id = id
        self.instructor = instructor
        self.tas = tas
        self.session = session
        self.description = description
        self.assignments = []
        self.meetings    = []
        self.annoucements = []
    
    def announce(self, annoucement):
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
