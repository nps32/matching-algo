from models.fellowApp import FellowApp
from models.tuteeApp import TuteeApp
from models.tutorSubj import TutorSubj
from models.tutorSubj import TutorSubj
from models.match import Match
from models.enums import * 
import heapq



def sortAllSubjectsByFellowCount(fellowApps): 
    # Dict which will have key = (Subject, Grade)
    tf_ref = [] 

    for fellow in fellowApps: 
        for subject in fellow.subjects: 
            for grade in fellow.grades: 
                if (subject, grade) in tf_ref:
                   # Add fellow id to pre-existing list 
                   curr_list = tf_ref[(subject,grade)]
                   curr_list.append(fellow.id)
                else: 
                    # Create new list of tf ids with this fellow's id 
                    tf_ref[(subject,grade)] = [fellow.id]

    return tf_ref 
                    



def createSubjHeap(tf_ref): 

    # Create heap 
    subj_heap = []

    # Iterate through every key-value pair in dict 
    for (subject, grade), id_list in tf_ref.items(): 
        if id_list is not None:  
            # Create and push onto heap for that (subject, grade) combination
            toPush = TutorSubj(subject, grade,len(id_list))
            heapq.heappush(subj_heap,toPush) 

    return subj_heap



"""
    STILL HAVE TO WRITE 
"""
def matchAvaliability(tutee, fellow): 
    return True

def updateMasterLists(matches): 
    return 




def matchSubjectChoice(fellows, tutees, tf_ref, subj_heap, eval): 
    
    matches = [] 
    scarceTutorSubj = heapq.heappop(subj_heap)

    grade = scarceTutorSubj.grade
    subject = scarceTutorSubj.subj 

    # Use list comprehension to filter new list of tutees having the same grade and subject-eval combo  
    matchingTutees = [tutee for tutee in tutees if (
            tutee.grade == subject and   
            (
                (tutee.subject1 == subject and tutee.eval1 == eval) or 
                (tutee.subject2 == subject and tutee.eval2 == eval) or 
                (tutee.subject3 == subject and tutee.eval3 == eval) 
            ) 
    )] 
    
    listOfIds = tf_ref[(subject,grade)]

    if listOfIds is not None:  
        #Use list comprehension to filter list of fellows with matching ids as in the dict 
        matchingFellows = [fellow for fellow in fellows if fellow.id in listOfIds]  
    else: 
        # SHOULD CONVERT TO LOGGING  
        print(f"No eligible teaching fellows for {subject}-{grade} combination")

    # NOW HAVE LIST OF 'MATCHING' TUTEES & TFs' for a subj-grd-eval combo 
    for tutee in matchingTutees: 
        for fellow in matchingFellows: 
            # NECESSARY TO CHECK matchCount? 
            if matchAvaliability(tutee, fellow) and (fellow.matchCount < 2):  
                match = Match(tf_id=fellow.id, tutee_id=tutee.id, subject=subject, grade=grade, cycle=fellow.cycle)
                matches.append(match)

    return matches 