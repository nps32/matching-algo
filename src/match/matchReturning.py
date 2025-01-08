
from typing import List
from src.models.fellowApp import FellowApp
from src.models.tuteeApp import TuteeApp
from src.models.match import Match


def matchReturning(tutees : List[TuteeApp], fellows : List[FellowApp]): 
  
  # Stores the created matches from pairing Returning TFs and Tutees 
  matches = []

  tuteeMap = {tutee.id: tutee for tutee in tutees}

  for fellow in fellows: 
    if fellow.wants_prev_tutee == True and fellow.match_count < fellow.capacity: 
        if fellow.prev_tutee_id in tuteeMap: 
            tutee = tuteeMap[fellow.prev_tutee_id]

            if tutee.wants_prev_fellow: 
                # Assign the match the subject the tutee needs most help in
                evaluations = [(tutee.subject1, tutee.eval1),(tutee.subject2, tutee.eval2),(tutee.subject3, tutee.eval3)]
                lowestSubject, _ = min(evaluations, key=lambda x: x[1])

                match = Match(
                    tf_id = fellow.id,
                    tutee_id = tutee.id, 
                    subject = lowestSubject,
                    grade = tutee.grade,
                    cycle = tutee.cycle 
                )

            fellow.match_count += 1  
            tutee.match_count += 1 

  return tutees, fellows, matches 