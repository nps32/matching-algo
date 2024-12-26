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

    def __str__(self):
        return (
            "Match Information:\n"
            f"Teaching Fellow ID: {self.tf_id if self.tf_id is not None else 'None'}\n"
            f"Tutee ID: {self.tutee_id if self.tutee_id is not None else 'None'}\n"
            f"Subject: {self.subject if self.subject is not None else 'None'}\n"
            f"Grade: {self.grade if self.grade is not None else 'None'}\n"
            f"Cycle: {self.cycle if self.cycle is not None else 'None'}" 
        )