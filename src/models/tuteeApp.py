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

     def printTutee(self):
        print("Tutee Information:")
        print(f"ID: {self.id}")
        print(f"Cycle: {self.cycle}")
        print(f"Availability: {self.availability}")
        print(f"Grade: {self.grade.value}")

        print("Subject Needs:")
        print(f"Subject 1: {self.subject1.value}, Evaluation 1: {self.eval1}")
        print(f"Subject 2: {self.subject2.value}, Evaluation 2: {self.eval2}")
        print(f"Subject 3: {self.subject3.value}, Evaluation 3: {self.eval3}")

        print("Capacity Information:")
        print(f"Match Count: {self.match_count}")
        print(f"Capacity: {self.capacity}")

        print("Returning Tutee Preferences:")
        print(f"Wants Previous Fellow: {self.wants_prev_fellow}")
        print(f"Previous Fellow Name: {self.prev_fellow_name}")
        print(f"Previous Fellow ID: {self.prev_fellow_id}")

# Example usage
tutee_instance = TuteeApp(id=1, cycle=Cycle.SPR24, availability=[Day.MON,Day.TUE, Day.FRI, Day.SAT], grade=Grade.MI, subject1=Subject.SAT_MATH, eval1=1, subject2=Subject.BIO, eval2=3, subject3=Subject.CHEM, eval3=4, match_count=0, capacity=2, wants_prev_fellow=False, prev_fellow_name="Diego", prev_fellow_id=2)
tutee_instance.printTutee()
