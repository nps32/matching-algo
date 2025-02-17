from src.models.enums.Grade import Grade
from src.models.enums.Subject import Subject

class AvailableTF: 
    """
    Represents the number of available teaching fellows for a given subject and grade combination.
    This class is used within matchByChoice for heap operations to determine the most scarce combination.
    """
    def __init__(self, subject, grade, available_tfs):
        self.subject = subject
        self.grade = grade
        self.available_tfs = available_tfs

    def __lt__(self, other):
        """
        Defines the less-than (<) comparison for heap operations.
        """
        return self.available_tfs < other.available_tfs

    def __str__(self):
        """
        Defines string representation for AvailableTF object.
        """
        return (
            "TutorSubj heap object:\n"
            f"Subject: {self.subject.value}\n"
            f"Grade: {self.grade.value}\n"
            f"Number of available TFs: {self.available_tfs}"
        )