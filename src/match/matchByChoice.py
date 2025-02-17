"""
The functions defined in this file represent the matchByChoice algorithm, broken down into helper functions.
For more information about the matchByChoice algorithm, see documentation: https://tinyurl.com/hatch-matching-algo.
"""

import heapq
from typing import Dict, List  
from src.models.availableTF import AvailableTF
from src.models.match import Match 
from src.models.fellowApp import FellowApp   
from src.models.tuteeApp import TuteeApp    


def sortAllSubjectsByFellowCount(fellowApps: List[FellowApp]) -> Dict[tuple, List[str]]:
    """
    Creates a dictionary mapping (subject, grade) to a list of eligible fellow application IDs.
    This dict is later used to construct the AvailableTF heap and for determining eligible 
    fellows for specific subject-grade combinations.
    """
    tf_ref: Dict[tuple, List[str]] = {}

    for fellowApp in fellowApps:
        for subject in fellowApp.subjects:
            for grade in fellowApp.grades:
                if (subject, grade) in tf_ref:
                    tf_ref[(subject, grade)].append(fellowApp.id)
                else:
                    tf_ref[(subject, grade)] = [fellowApp.id]

    return tf_ref 


def createSubjHeap(tf_ref: Dict[tuple, List[str]]) -> List[AvailableTF]:  
    """
    Creates a min-heap of subject-grade combinations based on the number of eligible teaching fellows.
    """
    subj_heap: List[AvailableTF] = []

    for (subject, grade), id_list in tf_ref.items(): 
        if id_list:  
            heapq.heappush(subj_heap, AvailableTF(subject, grade, len(id_list))) 

    return subj_heap


def matchAvailability(tuteeAvailability: List[str], fellowAvailability: List[str]) -> bool:  
    """
    Checks if a tutee and a fellow have overlapping availability. 
    """
    return any(tutee_day == fellow_day for tutee_day in tuteeAvailability for fellow_day in fellowAvailability)


def matchSubjectChoice(
    fellowApps: List[FellowApp], 
    tuteeApps: List[TuteeApp], 
    tf_ref: Dict[tuple, List[str]], 
    subj_heap: List[AvailableTF], 
    eval: int, 
    maxCap: int
) -> List[Match]:  
    """
    In order of subject-grade teaching fellow scarcity and subject eval for tutees, matches
    tutees and fellows, checking for availability. 
    """
    matches: List[Match] = []

    # While there are still subject-grade combinations to pair 
    while subj_heap:
        # Pop the current combination with the least eligible fellows off the heap
        scarce_availableTF = heapq.heappop(subj_heap)
        scarce_grade, scarce_subject = scarce_availableTF.grade, scarce_availableTF.subject 

        # Filter the list of tutees requesting that combination with the same eval
        matching_tutee_apps = [
            tuteeApp for tuteeApp in tuteeApps 
            if (tuteeApp.grade == scarce_grade and tuteeApp.match_count < maxCap) and (
                (tuteeApp.subject1 == scarce_subject and tuteeApp.eval1 == eval) or 
                (tuteeApp.subject2 == scarce_subject and tuteeApp.eval2 == eval) or 
                (tuteeApp.subject3 == scarce_subject and tuteeApp.eval3 == eval) 
            ) 
        ]  

        # If no tutees require that subject-grade combination, proceed to the next one
        if not matching_tutee_apps:
            continue

        # Retrieve list of eligible fellows
        list_of_ids = tf_ref.get((scarce_subject, scarce_grade), [])

        matching_fellow_apps = [
            fellowApp for fellowApp in fellowApps 
            if fellowApp.match_count < maxCap and fellowApp.id in list_of_ids
        ]  

        for fellowApp in matching_fellow_apps:
            # If no eligible fellows for subject-grade combination
            if not matching_fellow_apps:
                break
            for tuteeApp in matching_tutee_apps: 
                # If they are both available on at least one day of the week
                if matchAvailability(tuteeApp.availability, fellowApp.availability):  
                    # Record match
                    match = Match(tf_id=fellowApp.id, 
                                  tutee_id=tuteeApp.id, 
                                  subject=scarce_subject, 
                                  grade=scarce_grade, 
                                  cycle=fellowApp.cycle)

                    matches.append(match)

                    # Update capacity information for fellows and tutees 
                    tuteeApp.match_count += 1
                    fellowApp.match_count += 1

                    # Remove matched tutee for future iterations of the loop
                    matching_tutee_apps.remove(tuteeApp)

    return matches  


def matchByChoice(fellowApps: List[FellowApp], tuteeApps: List[TuteeApp], eval: int, maxCap: int) -> List[Match]:  
    """
    Master function which employs the others as helpers.
    """
    fellowApps = sorted(fellowApps, key=lambda x: x.returning, reverse=True) # pair returning fellows first 
    tf_ref = sortAllSubjectsByFellowCount(fellowApps)
    subj_heap = createSubjHeap(tf_ref)
    matches = matchSubjectChoice(fellowApps, tuteeApps, tf_ref, subj_heap, eval, maxCap)
    return matches