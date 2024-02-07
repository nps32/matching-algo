from enums import Grade
from enums import Subject

class TutorSubj: 
    def __init__(self, subject, grade, available_tfs): 
        self.subject = subject
        self.grade = grade 
        self.available_tfs = available_tfs

    def printTutorSubj(self):
        print("TutorSubj heap object:")
        print(f"Subject: {self.subject.value}")
        print(f"Grade: {self.grade.value}")
        print(f"Number of available TFs: {self.available_tfs}")

    # Define comparator method so heappq works as expected 
    def __lt__(self, other):
        return self.available_tfs < other.available_tfs

tutorSubj_instance =  TutorSubj(subject=Subject.CALC, grade=Grade.HS, available_tfs=24)

tutorSubj_instance.printTutorSubj()