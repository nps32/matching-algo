from src.models.enums.Grade import Grade
from src.models.enums.Subject import Subject

class AvailableTF: 
    def __init__(self, subject, grade, available_tfs): 
        self.subject = subject
        self.grade = grade 
        self.available_tfs = available_tfs

    def printAvailableTF(self):
        print("TutorSubj heap object:")
        print(f"Subject: {self.subject.value}")
        print(f"Grade: {self.grade.value}")
        print(f"Number of available TFs: {self.available_tfs}")

    # Define comparator method so heappq works as expected 
    def __lt__(self, other):
        return self.available_tfs < other.available_tfs

tutorSubj_instance =  AvailableTF(subject=Subject.CALC, grade=Grade.HS, available_tfs=24)

tutorSubj_instance.printAvailableTF()