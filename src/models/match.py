from src.models.enums.Cycle import Cycle
from src.models.enums.Subject import Subject
from src.models.enums.Grade import Grade

class Match: 
    """
    Represents a match between a teaching fellow and tutee for a given subject and grade level during the cycle.   
    This class is used to record the output of the matching process and is posted to the Wix CMS.   
    """
    def __init__(self, tf_id, tutee_id, subject, grade, cycle): 
        self.tf_id = tf_id 
        self.tutee_id = tutee_id
        self.subject = subject 
        self.grade = grade 
        self.cycle = cycle 

    def __str__(self):
        """
        Defines string representation for match object. 
        """
        return (
            "Match Information:\n"
            f"Teaching Fellow ID: {self.tf_id or 'Unknown'}\n"
            f"Tutee ID: {self.tutee_id or 'Unknown'}\n"
            f"Subject: {self.subject or 'Unknown'}\n"
            f"Grade: {self.grade or 'Unknown'}\n"
            f"Cycle: {self.cycle or 'Unknown'}"
        )