
import pytest 
import heapq 

from src.match.matchByChoice import sortAllSubjectsByFellowCount
from src.match.matchByChoice import matchAvailability
from src.match.matchByChoice import createSubjHeap
from src.models.enums.Day import Day
from src.models.enums.Cycle import Cycle 
from src.models.enums.Grade import Grade 
from src.models.enums.Subject import Subject
from src.models.fellowApp import FellowApp


def testCheckAvailability():
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


# Create dummy object for use in test_createSubjectHeap
@pytest.fixture
def tf_ref(): 
    return  {
    (Subject.CALC, Grade.HS): [1, 2, 3],
    (Subject.BIO, Grade.MI): [4, 5],
    (Subject.EN_READ, Grade.LE): [6],
    (Subject.CS, Grade.HS): [1, 2, 9, 4],  
    (Subject.SAT, Grade.HS): None }


def test_createSubjHeap(tf_ref):

    heap = createSubjHeap(tf_ref)

    # Check if the heap has the correct number of elements
    assert len(heap) == 4

    # Check if the heap is in the correct state through successive pops 
    top = heapq.heappop(heap)
    assert top.available_tfs == 1
    assert top.subject == Subject.EN_READ
    assert top.grade == Grade.LE

    top = heapq.heappop(heap)
    assert top.available_tfs == 2
    assert top.subject == Subject.BIO
    assert top.grade == Grade.MI

    top = heapq.heappop(heap)
    assert top.available_tfs == 3
    assert top.subject == Subject.CALC
    assert top.grade == Grade.HS

    top = heapq.heappop(heap)
    assert top.available_tfs == 4
    assert top.subject == Subject.CS
    assert top.grade == Grade.HS

    # asserts heap is now empty
    with pytest.raises(IndexError):
        heapq.heappop(heap)

# Create dummy object for use in test_createSubjectHeap
@pytest.fixture
def tf_ref2(): 
    return  {
    (Subject.CALC, Grade.HS): None,
    (Subject.BIO, Grade.MI): None,
    (Subject.EN_READ, Grade.LE): None,
    (Subject.CS, Grade.HS): None,  
    (Subject.SAT, Grade.HS): None }

def test_createSubjHeapEmpty(tf_ref2): 
    heap = createSubjHeap(tf_ref2) 
    
    # asserts heap created is empty 
    with pytest.raises(IndexError):
        heapq.heappop(heap)

# Create dummy object for use in test_sortAllSubjectsByFellowCount()
@pytest.fixture
def fellow_apps():
    # Create mock FellowApp instances with varying capacities, match_count, and multiple grades
    fellow1 = FellowApp(id=1, cycle=Cycle.FALL23, availability=[Day.MON, Day.WED], grades=[Grade.HS, Grade.MI], subjects=[Subject.MATH2ALG, Subject.PHYSICS], match_count=1, capacity=2)
    fellow2 = FellowApp(id=2, cycle=Cycle.FALL23, availability=[Day.TUE, Day.FRI], grades=[Grade.MI], subjects=[Subject.MATH2ALG, Subject.CHEM, Subject.EN_READ], match_count=1, capacity=1)
    fellow3 = FellowApp(id=3, cycle=Cycle.FALL23, availability=[Day.MON, Day.FRI], grades=[Grade.HS], subjects=[Subject.PHYSICS, Subject.CHEM], match_count=0, capacity=2)
    fellow4 = FellowApp(id=4, cycle=Cycle.FALL23, availability=[Day.TUE], grades=[Grade.MI, Grade.HS], subjects=[Subject.CHEM, Subject.PHYSICS], match_count=0, capacity=1)
    
    return [fellow1, fellow2, fellow3, fellow4]

# Create dummy object for use in test_sortAllSubjectsByFellowCount()
@pytest.fixture
def expected_tf_ref():
    # Expected tf_ref dictionary reflecting the fellows eligible to teach multiple grades
    return {
        (Subject.MATH2ALG, Grade.MI): [1, 2],   # Fellows 1 and 2 can teach MATH2ALG for Grade.MI
        (Subject.MATH2ALG, Grade.HS): [1],      # Fellow  1 can teach MATH2ALG for Grade.HS
        (Subject.CHEM, Grade.MI): [2, 4],       # Fellows 2 and 4 can teach CHEM for Grade.MI
        (Subject.CHEM, Grade.HS): [3, 4],       # Fellows 3 and 4 can teach CHEM for Grade.HS 
        (Subject.PHYSICS, Grade.MI): [1, 4],    # Fellows 4 and 1 can teach PHYSICS for Grade.MI
        (Subject.PHYSICS, Grade.HS): [1, 3, 4], # Fellows 1,3,4 can teach PHYSICS for Grade.HS
        (Subject.EN_READ, Grade.MI): [2]        # Fellow 2 can teach EN_READ for Grade.MI
    }

def test_sortAllSubjectsByFellowCount(fellow_apps, expected_tf_ref):
    tf_ref = sortAllSubjectsByFellowCount(fellow_apps)

    # Assert that the proper number of unique Subject-Grade combinations are generated 
    assert len(expected_tf_ref) == 7

     # Assert that tf_ref matches the expected values
    for key, fellow_ids in expected_tf_ref.items():
        assert key in tf_ref, f"Missing key: {key}"
        assert sorted(tf_ref[key]) == sorted(fellow_ids), f"Values for {key} don't match. Expected {fellow_ids}, but got {tf_ref[key]}" 




@pytest.fixture 
def fellowApps2(): 
    return [
        FellowApp(id=2, cycle=Cycle.FALL23, availability=[Day.MON, Day.WED], grades=[Grade.HS, Grade.MI], subjects=[Subject.MATH2ALG, Subject.PHYSICS], match_count=1, capacity=2),
        FellowApp(id=3, cycle=Cycle.FALL23, availability=[Day.MON, Day.WED], grades=[Grade.HS, Grade.MI], subjects=[Subject.MATH2ALG, Subject.PHYSICS], match_count=1, capacity=2),
        FellowApp(id=4, cycle=Cycle.FALL23, availability=[Day.MON, Day.WED], grades=[Grade.HS, Grade.MI], subjects=[Subject.MATH2ALG, Subject.PHYSICS], match_count=1, capacity=2) ]

@pytest.fixture 
def tuteeApps(): 
    return [
        TuteeApp(id=1, cycle=Cycle.SPR24, availability=[Day.MON,Day.TUE, Day.FRI, Day.SAT], grade=Grade.MI, subject1=Subject.SAT_MATH, eval1=1, subject2=Subject.BIO, eval2=3, subject3=Subject.CHEM, eval3=4, match_count=0, capacity=2, wants_prev_fellow=False, prev_fellow_name="Diego", prev_fellow_id=2)
    ] 

@pytest.fixture 
def tf_ref3(fellowApps2): 
    return sortAllSubjectsByFellowCount(fellowApps2)
    
@pytest.fixture 
def subj_heap(tf_ref3): 
    return createSubjHeap(tf_ref3)

#def testMatchSubjectChoice(fellowApps, tuteeApps, tf_ref, subj_heap, eval, maxCap):       
