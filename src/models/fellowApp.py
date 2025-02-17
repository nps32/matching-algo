from src.models.enums.Subject import Subject 
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle
from src.models.enums.Day import Day


class FellowApp:
     """
     Represents an application by a teaching fellow to tutor for a given cycle. 
     This class holds all information necessary to create a match with a tutee and is serialized from Wix CMS data.
     """
     def __init__(
        self, 
        id, 
        cycle, 
        availability, 
        grades, 
        subjects, 
        match_count, 
        capacity, 
        returning=False, 
        wants_prev_tutee=None, 
        prev_tutee_name=None, 
        prev_tutee_id=None
    ):
        # Tutoring information
        self.id = id
        self.cycle = cycle
        self.availability = availability
        self.grades = grades
        self.subjects = subjects

        # Capacity information
        self.capacity = capacity
        self.match_count = match_count

        # Returning fellows information
        self.returning = returning
        self.wants_prev_tutee = wants_prev_tutee
        self.prev_tutee_name = prev_tutee_name
        self.prev_tutee_id = prev_tutee_id


        def __str__(self):
            """
            Defines string representation for teaching fellow application object. 
            """
            return (
                "Fellow Information:\n"
                f"ID: {self.id or 'Unknown'}\n"
                f"Cycle: {self.cycle or 'Unknown'}\n"
                f"Availability: {self.availability}\n\n"

                "Tutoring Ability:\n"
                f"Grades: {self.grades}\n"
                f"Subjects: {self.subjects}\n"
                f"Capacity: {self.capacity or 'Unknown'}\n"
                f"Match Count: {self.match_count or 'Unknown'}\n\n"

                "Returning Fellow Preferences:\n"
                f"Returning Fellow? {self.returning}\n"
                f"Wants Previous Tutee: {self.wants_prev_tutee}\n"
                f"Previous Tutee Name: {self.prev_tutee_name or 'Unknown'}\n"
                f"Previous Tutee ID: {self.prev_tutee_id or 'Unknown'}"
            )