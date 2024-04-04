from match.matchByChoice import matchAvailability
from src.models.enums import Day

import pytest


class TestMatchingAlgo():
    def testCheckAvailability(self):
        #Should match on Mon
        tuteeAvailability = [Day.MON, Day.WED, Day.FRI]
        fellowAvailability = [Day.MON, Day.SAT, Day.TUE]
        assert matchAvailability(tuteeAvailability, fellowAvailability) == True
