from src.models.enums.Subject import Subject 
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle
from src.models.enums.Day import Day


class FellowApp:

    def __init__(self, id, cycle, availability, grades, subjects, match_count, capacity, returning=False, wants_prev_tutee=None, prev_tutee_name=None, prev_tutee_id=None):
        self.id = id #primary key 
        self.cycle = cycle
        self.availability = availability 
        self.grades = grades 
        self.subjects = subjects
        

        #Capacity info 
        self.capacity = capacity
        self.match_count = match_count

        #For returning TFs 
        self.returning = returning
        self.wants_prev_tutee = wants_prev_tutee
        self.prev_tutee_name = prev_tutee_name
        self.prev_tutee_id = prev_tutee_id

    def __str__(self):
        return (
            "Fellow Information:\n"
            f"ID: {self.id if self.id is not None else 'None'}\n"
            f"Cycle: {self.cycle if self.cycle is not None else 'None'}\n"
            f"Availability: {self.availability}\n\n"

            "Tutoring Ability:\n"
            f"Grades: {self.grades}\n"
            f"Subjects: {self.subjects}\n"
            f"Capacity: {self.capacity if self.capacity is not None else 'None'}\n"
            f"Match Count: {self.match_count if self.match_count is not None else 'None'}\n\n"

            "Returning Fellow Preferences:\n"
            f"Returning Fellow? {self.returning}\n"
            f"Wants Previous Tutee: {self.wants_prev_tutee}\n"
            f"Previous Tutee Name: {self.prev_tutee_name if self.prev_tutee_name is not None else 'None'}\n"
            f"Previous Tutee ID: {self.prev_tutee_id if self.prev_tutee_id is not None else 'None'}"
        )