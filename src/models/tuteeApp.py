from src.models.enums.Subject import Subject
from src.models.enums.Day import Day
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle

class TuteeApp:

     def __init__(self, id, cycle, availability, grade, subject1, eval1, subject2, eval2, subject3, eval3, match_count, capacity, wants_prev_fellow=None, prev_fellow_name=None, prev_fellow_id=None):
        self.id = id #primary key 
        self.cycle = cycle
        self.availability = availability 
        self.grade = grade

        #subject needs 
        self.subject1 = subject1 
        self.eval1 = eval1 
        self.subject2 = subject2
        self.eval2 = eval2
        self.subject3 = subject3
        self.eval3 = eval3 

        #Capacity info 
        self.match_count = match_count 
        self.capacity = capacity

        #For returning TFs 
        self.wants_prev_fellow = wants_prev_fellow 
        self.prev_fellow_name = prev_fellow_name 
        self.prev_fellow_id = prev_fellow_id

     def __str__(self):
         return (
            "Tutee Information:\n"
            f"ID: {self.id}\n"
            f"Cycle: {self.cycle}\n"
            f"Availability: {self.availability}\n"
            f"Grade: {self.grade.value}\n\n"

            "Subject Needs:\n"
            f"Subject 1: {self.subject1.value}, Evaluation 1: {self.eval1}\n"
            f"Subject 2: {self.subject2.value}, Evaluation 2: {self.eval2}\n"
            f"Subject 3: {self.subject3.value}, Evaluation 3: {self.eval3}\n\n"

            "Capacity Information:\n"
            f"Match Count: {self.match_count}\n"
            f"Capacity: {self.capacity}\n\n"

            "Returning Tutee Preferences:\n"
            f"Wants Previous Fellow: {self.wants_prev_fellow}\n"
            f"Previous Fellow Name: {self.prev_fellow_name}\n"
            f"Previous Fellow ID: {self.prev_fellow_id}\n"
         )

     def __str__(self):
        return (
            "Tutee Information:\n"
            f"ID: {self.id if self.id is not None else 'None'}\n"
            f"Cycle: {self.cycle if self.cycle is not None else 'None'}\n"
            f"Availability: {self.availability}\n"
            f"Grade: {self.grade.value if self.grade is not None else 'None'}\n\n"

            "Subject Needs:\n"
            f"Subject 1: {self.subject1.value if self.subject1 is not None else 'None'}, Evaluation 1: {self.eval1 if self.eval1 is not None else 'None'}\n"
            f"Subject 2: {self.subject2.value if self.subject2 is not None else 'None'}, Evaluation 2: {self.eval2 if self.eval2 is not None else 'None'}\n"
            f"Subject 3: {self.subject3.value if self.subject3 is not None else 'None'}, Evaluation 3: {self.eval3 if self.eval3 is not None else 'None'}\n\n"

            "Capacity Information:\n"
            f"Match Count: {self.match_count if self.match_count is not None else 'None'}\n"
            f"Capacity: {self.capacity if self.capacity is not None else 'None'}\n\n"

            "Returning Tutee Preferences:\n"
            f"Wants Previous Fellow: {self.wants_prev_fellow}\n"
            f"Previous Fellow Name: {self.prev_fellow_name if self.prev_fellow_name is not None else 'None'}\n"
            f"Previous Fellow ID: {self.prev_fellow_id if self.prev_fellow_id is not None else 'None'}\n"
        )
