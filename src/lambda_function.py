import logging
from src.api.requester import Requester
from src.match.matchByChoice import matchByChoice
from src.match.matchReturning import matchReturning
from src.models.enums.Cycle import Cycle

# Configure logging for CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Conducts the overarching process of matching:
    
    1. Pulling the FellowApp and TuteeApp data for the current cycle.
    2. Matching consenting returning fellows with their tutees.
    3. General matching (`matchByChoice`), prioritizing fellows with fewer existing matches and 
       subjects requiring more assistance.
    4. Updating the Wix CMS with match data and updated capacity information for tutees and teaching fellows.
    """
    try:
        logger.info("Lambda function execution started.")
        
        """# Extracting cycle information
        body = event.get("body", {})   
        cycle_text = body.get("cycle", Cycle.TEST)
        logger.info(f"Cycle retrieved from event: {cycle_text}")"""

        requester = Requester()

        # Fetch applications
        logger.info("Fetching Fellow and Tutee applications...")
        fellows = requester.getFellowApps(Cycle.TEST)
        tutees = requester.getTuteeApps(Cycle.TEST)

        # Match returning fellows
        logger.info("Starting returning fellows matching process...")
        tutees, fellows, matches = matchReturning(fellowApps=fellows, tuteeApps=tutees)
        logger.info(f"Matches after returning fellows process: {len(matches)}.")

        # Perform matchByChoice with different parameters
        for max_cap in (1, 2):
            for eval_score in (1, 6):
                logger.info(f"MatchByChoice with maxCap={max_cap}, eval={eval_score}...")
                new_matches = matchByChoice(fellowApps=fellows, tuteeApps=tutees, eval=eval_score, maxCap=max_cap)
                matches.extend(new_matches)
                logger.info(f"Added {len(new_matches)} new matches, total matches now: {len(matches)}.")

        # Update Wix CMS with new matches
        logger.info("Updating Wix CMS with {len(matches)} new matches")
        requester.updateFellows(fellows, cycle=Cycle.TEST)
        requester.updateTutees(tutees, cycle=Cycle.TEST)
        requester.postMatches(matches)

        logger.info(f"Final total matches: ")
        
        return # {"statusCode": 200, "body": "Matching process completed successfully"} #TODO: necessary?

    except Exception as e:
        logger.error(f"An error occurred during matching:\n {str(e)}", exc_info=True)
        return # {"statusCode": 500, "body": "Internal Server Error"} #TODO: necessary?

    finally:
        logger.info("Lambda function execution completed.")