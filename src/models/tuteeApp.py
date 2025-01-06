from src.models.enums.Subject import Subject
from src.models.enums.Day import Day
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle

class TuteeApp:

     def __init__(self, id, cycle, availability, grade, subject1, eval1, subject2, eval2, subject3, 
     eval3, match_count, capacity, wants_prev_fellow=None, prev_fellow_name=None, prev_fellow_id=None):
        # Key info
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

        # Capacity info
        self.match_count = match_count 
        self.capacity = capacity

        # Returning tutees 
        self.wants_prev_fellow = wants_prev_fellow 
        self.prev_fellow_name = prev_fellow_name 
        self.prev_fellow_id = prev_fellow_id


     def replaceNone(self, val) -> str: 
        if val is None: 
            return 'None'
        else: 
            return val


     def __str__(self):
        return (
            "Tutee Information:\n"
            f"ID: {self.replaceNone(self.id)}\n"
            f"Cycle: {self.replaceNone(self.cycle)}\n"
            f"Availability: {self.availability}\n"
            f"Grade: {self.replaceNone(self.grade.value)}\n\n"

            "Subject Needs:\n"
            f"Subject 1: {self.replaceNone(self.subject1.value)}, Evaluation 1: {self.replaceNone(self.eval1)}\n"
            f"Subject 2: {self.replaceNone(self.subject2.value)}, Evaluation 2: {self.replaceNone(self.eval2)}\n"
            f"Subject 3: {self.replaceNone(self.subject3.value)}, Evaluation 3: {self.replaceNone(self.eval3)}\n\n"

            "Capacity Information:\n"
            f"Match Count: {self.replaceNone(self.match_count)}\n"
            f"Capacity: {self.replaceNone(self.capacity)}\n\n"

            "Returning Tutee Preferences:\n"
            f"Wants Previous Fellow: {self.wants_prev_fellow}\n"
            f"Previous Fellow Name: {self.replaceNone(self.prev_fellow_name)}\n"
            f"Previous Fellow ID: {self.replaceNone(self.prev_fellow_id)}\n"
        )
