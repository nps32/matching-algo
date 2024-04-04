from enums import Cycle
from enums import Subject
from enums import Grade

class Match: 
    def __init__(self, tf_id, tutee_id, subject, grade, cycle): 
        self.tf_id = tf_id 
        self.tutee_id = tutee_id
        self.subject = subject 
        self.grade = grade 
        self.cycle = cycle 

    def printMatch(self):
        print("Match Information:")
        print(f"Teaching Fellow ID: {self.tf_id}")
        print(f"Tutee ID: {self.tutee_id}")
        print(f"Subject: {self.subject}")
        print(f"Grade: {self.grade}")
        print(f"Cycle: {self.cycle}")

# Example usage
match_instance = Match(tf_id=1, tutee_id=101, subject=Subject.BIO.value, grade=Grade.LE.value, cycle=Cycle.FALL23.value)
match_instance.printMatch()