from src.models.enums.Subject import Subject 
from src.models.enums.Grade import Grade
from src.models.enums.Cycle import Cycle
from src.models.enums.Day import Day


class FellowApp:

    def __init__(self, id, cycle, availability, grades, subjects, match_count, capacity, wants_prev_tutee=None, prev_tutee_name=None, prev_tutee_id=None):
        self.id = id #primary key 
        self.cycle = cycle
        self.availability = availability 
        self.grades = grades 
        self.subjects = subjects

        #Capacity info 
        self.capacity = capacity
        self.match_count = match_count

        #For returning TFs 
        self.wants_prev_tutee = wants_prev_tutee
        self.prev_tutee_name = prev_tutee_name
        self.prev_tutee_id = prev_tutee_id

    def printFellow(self):
        print("Fellow Information:")
        print(f"ID: {self.id}")
        print(f"Cycle: {self.cycle}")
        print(f"Availability: {self.availability}")
        print(f"Grades: {self.grades}")
        print(f"Subjects: {self.subjects}")
        print(f"Match Count: {self.match_count}")
        print(f"Capacity: {self.capacity}")
        print(f"Wants Previous Tutee: {self.wants_prev_tutee}")
        print(f"Wants Previous Tutee: {self.prev_tutee_name}")
        print(f"Previous Tutee ID: {self.prev_tutee_id}")

# Example usage
fellow_instance = FellowApp(id=1, cycle=Cycle.FALL23, availability=[Day.MON, Day.WED, Day.FRI], grades=[Grade.MI, Grade.HS], subjects=[Subject.MATH2ALG, Subject.PHYSICS, Subject.CHEM, Subject.CHINESE], match_count=0, capacity=1, wants_prev_tutee=False, prev_tutee_name="Nav", prev_tutee_id=101)
fellow_instance.printFellow()