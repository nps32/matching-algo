from src.models.enums.Subject import Subject 
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle
from src.models.enums.Day import Day


class FellowApp:

    def __init__(self, id, cycle, availability, grades, subjects, match_count, capacity, 
    returning=False, wants_prev_tutee=None, prev_tutee_name=None, prev_tutee_id=None):
        # Key info
        self.id = id 
        self.cycle = cycle
        self.availability = availability 
        self.grades = grades 
        self.subjects = subjects
        
        #Capacity info 
        self.capacity = capacity
        self.match_count = match_count

        # Returning fellows 
        self.returning = returning
        self.wants_prev_tutee = wants_prev_tutee
        self.prev_tutee_name = prev_tutee_name
        self.prev_tutee_id = prev_tutee_id


    def replaceNone(self, val) -> str: 
        if val is None: 
            return 'None'
        else: 
            return val


    def __str__(self):
        return (
            "Fellow Information:\n"
            f"ID: {self.replaceNone(self.id)}\n"
            f"Cycle: {self.replaceNone(self.cycle)}\n"
            f"Availability: {self.availability}\n\n"

            "Tutoring Ability:\n"
            f"Grades: {self.grades}\n"
            f"Subjects: {self.subjects}\n"
            f"Capacity: {self.replaceNone(self.capacity)}\n"
            f"Match Count: {self.replaceNone(self.match_count)}\n\n"

            "Returning Fellow Preferences:\n"
            f"Returning Fellow? {self.returning}\n"
            f"Wants Previous Tutee: {self.wants_prev_tutee}\n"
            f"Previous Tutee Name: {self.replaceNone(self.prev_tutee_name)}\n"
            f"Previous Tutee ID: {self.replaceNone(self.prev_tutee_id)}"
        )