import heapq

from src.models.availableTF import AvailableTF
from src.models.match import Match 


def sortAllSubjectsByFellowCount(fellowApps):
    # Dict which will have key = (Subject, Grade)
    tf_ref = dict()

    for fellowApp in fellowApps:
        for subject in fellowApp.subjects:
            for grade in fellowApp.grades:
                if (subject, grade) in tf_ref:
                   # Add fellow id to pre-existing list
                   curr_list = tf_ref[(subject,grade)]
                   curr_list.append(fellowApp.id)
                else:
                    # Create new list of tf ids with this fellow's id
                    tf_ref[(subject,grade)] = [fellowApp.id]

    return tf_ref 


def createSubjHeap(tf_ref): 

    # Create heap 
    subj_heap = []

    # Iterate through every key-value pair in dict 
    for (subject, grade), id_list in tf_ref.items(): 
        if id_list is not None:  
            # Create and push onto heap for that (subject, grade) combination
            toPush = AvailableTF(subject, grade,len(id_list))
            heapq.heappush(subj_heap,toPush) 

    return subj_heap


def matchAvailability(tuteeAvailability, fellowAvailability): 
    for tDay in tuteeAvailability: 
        for fDay in fellowAvailability: 
            if (tDay == fDay): 
                return True 
    return False 


def matchSubjectChoice(fellowApps, tuteeApps, tf_ref, subj_heap, eval, maxCap): 
    
    matches = []  

    while (len(subj_heap) != 0): 
        
        scarceAvailableTF = heapq.heappop(subj_heap)
        scarceGrade = scarceAvailableTF.grade
        scarceSubject = scarceAvailableTF.subject 

        # Use list comprehension to filter tutees having the same grade and subject-eval combo and appropriate match count
        matchingTuteeApps = [tuteeApp for tuteeApp in tuteeApps if (
            (tuteeApp.grade == scarceGrade) and 
            (tuteeApp.matchCount < maxCap) and 
            (
                (tuteeApp.subject1 == scarceSubject and tuteeApp.eval1 == eval) or 
                (tuteeApp.subject2 == scarceSubject and tuteeApp.eval2 == eval) or 
                (tuteeApp.subject3 == scarceSubject and tuteeApp.eval3 == eval) 
            ) 
        )] 
    
        # Skips subject-grade combination if no matching tutees for subj-grd-eval combination 
        if len(matchingTuteeApps) == 0: 
            continue

        # Get corresponding list of TF ids from tf_ref
        listOfIds = tf_ref[(scarceSubject,scarceGrade)]

        #Use list comprehension to filter fellows with matching ids and appropriate match count
        matchingFellowApps = [fellowApp for fellowApp in fellowApps if ( 
                                    fellowApp.matchCount < maxCap and 
                                    fellowApp.id in listOfIds
                              )]  

        for fellowApp in matchingFellowApps:
            if len(matchingTuteeApps) == 0: 
                break
            else: 
                for tuteeApp in matchingTuteeApps: 
                    if matchAvailability(tuteeApp.availability, fellowApp.availability):  
                        # Create match
                        match = Match(tf_id=fellowApp.id, tutee_id=tuteeApp.id, subject=scarceSubject, grade=scarceGrade, cycle=fellowApp.cycle)

                        #Add match
                        matches.append(match)

                        tuteeApp.match_count = tuteeApp.match_count + 1
                        fellowApp.match_count = fellowApp.match_count + 1

                        # Remove matched tuteeApp from pool for next iteration
                        matchingTuteeApps.remove(tuteeApp)
            
    return matches  


# Master function for the matchByChoice stage
def matchByChoice(fellowApps, tuteeApps, eval, maxCap): 

    tf_ref = sortAllSubjectsByFellowCount(fellowApps)
    subj_heap = createSubjHeap(tf_ref)
    matches = matchSubjectChoice(fellowApps, tuteeApps, tf_ref, subj_heap, eval, maxCap)

    return matches 