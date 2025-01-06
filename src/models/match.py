from src.models.enums.Cycle import Cycle
from src.models.enums.Subject import Subject
from src.models.enums.Grade import Grade

class Match: 
    def __init__(self, tf_id, tutee_id, subject, grade, cycle): 
        self.tf_id = tf_id 
        self.tutee_id = tutee_id
        self.subject = subject 
        self.grade = grade 
        self.cycle = cycle 

    def replaceNone(self, val) -> str: 
        if val is None: 
            return 'None'
        else: 
            return val

    def __str__(self):
        return (
            "Match Information:\n"
            f"Teaching Fellow ID: {self.replaceNone(self.tf_id)}\n"
            f"Tutee ID: {self.replaceNone(self.tutee_id)}\n"
            f"Subject: {self.replaceNone(self.subject)}\n"
            f"Grade: {self.replaceNone(self.grade)}\n"
            f"Cycle: {self.replaceNone(self.cycle)}" 
        )