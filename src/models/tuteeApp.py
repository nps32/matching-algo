from src.models.enums.Subject import Subject
from src.models.enums.Day import Day
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle


class TuteeApp:
    """
    Represents an application by a tutee to be tutored for a given cycle.
    This class holds all information necessary to create a match with a teaching fellow and is serialized from Wix CMS data.
    """    
    def __init__(
        self, 
        id, 
        cycle, 
        availability, 
        grade, 
        subject1, 
        eval1, 
        subject2, 
        eval2, 
        subject3, 
        eval3, 
        match_count, 
        capacity, 
        wants_prev_fellow=None, 
        prev_fellow_name=None, 
        prev_fellow_id=None
    ):
        # Key information 
        self.id = id
        self.cycle = cycle
        self.availability = availability
        self.grade = grade

        # Subject needs
        self.subject1 = subject1
        self.eval1 = eval1
        self.subject2 = subject2
        self.eval2 = eval2
        self.subject3 = subject3
        self.eval3 = eval3

        # Capacity information
        self.match_count = match_count
        self.capacity = capacity

        # Returning tutees
        self.wants_prev_fellow = wants_prev_fellow
        self.prev_fellow_name = prev_fellow_name
        self.prev_fellow_id = prev_fellow_id

    def __str__(self):
        """
        Defines string representation for tutee application object. 
        """
        return (
            "Tutee Information:\n"
            f"ID: {self.id or 'Unknown'}\n"
            f"Cycle: {self.cycle or 'Unknown'}\n"
            f"Availability: {self.availability}\n"
            f"Grade: {getattr(self.grade, 'value', 'Unknown')}\n\n"

            "Subject Needs:\n"
            f"Subject 1: {getattr(self.subject1, 'value', 'Unknown')}, Evaluation 1: {self.eval1 or 'Unknown'}\n"
            f"Subject 2: {getattr(self.subject2, 'value', 'Unknown')}, Evaluation 2: {self.eval2 or 'Unknown'}\n"
            f"Subject 3: {getattr(self.subject3, 'value', 'Unknown')}, Evaluation 3: {self.eval3 or 'Unknown'}\n\n"

            "Capacity Information:\n"
            f"Match Count: {self.match_count or 'Unknown'}\n"
            f"Capacity: {self.capacity or 'Unknown'}\n\n"

            "Returning Tutee Preferences:\n"
            f"Wants Previous Fellow: {self.wants_prev_fellow}\n"
            f"Previous Fellow Name: {self.prev_fellow_name or 'Unknown'}\n"
            f"Previous Fellow ID: {self.prev_fellow_id or 'Unknown'}\n"
        )