from src.match.matchByChoice import matchAvailability
from src.models.enums.Day import Day
from src.models.enums.Cycle import Cycle 
from src.models.enums.Grade import Grade 
from src.models.enums.Subject import Subject

class TestMatchingAlgo():

    def testCheckAvailability(self):
        #Should match on Mon
        tuteeAvailability = [Day.MON, Day.WED, Day.FRI]
        fellowAvailability = [Day.MON, Day.SAT, Day.TUE]
        assert matchAvailability(tuteeAvailability, fellowAvailability) == True

        #Should not match 
        tuteeAvailability = [Day.TUE] 
        fellowAvailability = [Day.MON] 
        assert matchAvailability(tuteeAvailability, fellowAvailability) == False

        #Should match on Tuesday
        tuteeAvailability = [Day.MON, Day.TUE, Day.WED, Day.THURS, Day.FRI, Day.SAT, Day.SUN] 
        fellowAvailability = [Day.TUE] 
        assert matchAvailability(tuteeAvailability, fellowAvailability) == True

        #Should match on Wednesday or Saturday
        tuteeAvailability = [Day.WED, Day.SAT] 
        fellowAvailability = [Day.TUE, Day.SAT, Day.WED] 
        assert matchAvailability(tuteeAvailability, fellowAvailability) == True 

        #Should match on Wednesday or Saturday
        tuteeAvailability = [Day.WED, Day.SAT] 
        fellowAvailability = [Day.TUE, Day.SAT, Day.WED] 
        assert matchAvailability(tuteeAvailability, fellowAvailability) == True

        #Should not match 
        tuteeAvailability = [Day.MON, Day.WED, Day.FRI, Day.SUN] 
        fellowAvailability = [Day.TUE, Day.THURS, Day.SAT] 
        assert matchAvailability(tuteeAvailability, fellowAvailability) == False 