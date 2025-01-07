
from src.api.requester import Requester
from src.match.matchByChoice import matchByChoice
from src.match.matchReturning import matchReturning
from src.models.enums.Cycle import Cycle 

def lambda_handler(event, context): 
    """
    Triggered by the call to the lambda function. Gets the tutee and fellow data from the Wix CMS, runs the appropriate 
    matching algorithms on it, and then updates the data in CMS, posting matches and updating match_counts for Tutees and Fellows
    """
    body = event.get('body', "No body provided") 
    cycleText = body['cycle'] 
    
    






    requester = Requester()

    fellows = requester.getFellowApps(Cycle.TEST) # need to sub in param for context 
    tutees = requester.getTuteeApps(Cycle.TEST) # need to sub in param for context 

    matches = matchReturning(fellowApps=fellows, tuteeApps=tutees)

    for maxCap in (1,2):
        for eval in (1,6): 
           matches.extend(matchByChoice(fellowApps=fellows, tuteeApps=tutees, eval=eval, maxCap=maxCap)) 

    requester.updateFellows(fellows, cycle=Cycle.TEST)
    requester.updateTutees(tutees, cycle=Cycle.TEST)
    requester.postMatches(matches) 