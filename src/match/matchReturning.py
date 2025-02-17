from typing import List
from src.models.fellowApp import FellowApp
from src.models.tuteeApp import TuteeApp
from src.models.match import Match


def matchReturning(tutees: List[TuteeApp], fellows: List[FellowApp]):
    """
    Matches returning teaching fellows (TFs) with their previous tutees if both consent.
    Returns tutees and fellows in addition to matches in order to preserve updated capacity information.
    """

    matches = []  

    # Map tutees by their ID for quick lookup
    tutee_map = {tutee.id: tutee for tutee in tutees}

    for fellow in fellows:
        if fellow.wants_prev_tutee and fellow.match_count < fellow.capacity:
            tutee = tutee_map.get(fellow.prev_tutee_id) #TODO: write script to provide fellow apps with prev_tutee_id in CMS 

            if tutee and tutee.wants_prev_fellow:
                # Determine the subject where the tutee needs the most help
                evaluations = [
                    (tutee.subject1, tutee.eval1),
                    (tutee.subject2, tutee.eval2),
                    (tutee.subject3, tutee.eval3),
                ]
                hardest_subject, _ = min(evaluations, key=lambda x: x[1])

                # Create a corresponding match object
                match = Match(
                    tf_id=fellow.id,
                    tutee_id=tutee.id,
                    subject=hardest_subject,
                    grade=tutee.grade,
                    cycle=tutee.cycle,
                )
                matches.append(match)

                # Update match counts for both fellow and tutee
                fellow.match_count += 1
                tutee.match_count += 1

    return tutees, fellows, matches