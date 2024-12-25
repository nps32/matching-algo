import json
import requests

from typing import Dict, List

from src.models.enums.Cycle import Cycle

from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp 
from src.models.match import Match

from src.utils.jsonConverters import convertJsonToTutees
from src.utils.jsonConverters import convertJsonToFellows


class Requester: 

    def __init__(self): 
        
        # URLs for Wix API Requests 
        self.queryUrl = r'https://www.wixapis.com/wix-data/v2/items/query'

        # Extract authToken from file in directory 
        with open('token.txt', 'r') as file:
            self.authToken = file.read().strip()     

        # Extract authToken from file in directory 
        with open('site-id.txt','r') as file: 
            self.siteId = file.read().strip()

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.authToken}',  
            'wix-site-id': f'{self.siteId}'
        }

        # Needed to request a specific Cycle 
        self.cycleIDs = {Cycle.TEST:"2bb261dd-2968-4c5b-bd05-731eaa7c3c87",
                         Cycle.SPR24:"613958f3-cd19-4604-902b-4fffacf28672"}


    def getFellowApps(self, cycle : Cycle) -> List[FellowApp]: 
         
        # Set parameters for request 
        data = {
            'dataCollectionId': "FellowApplications",
            'query': {
                'filter': {'cycle': f"{self.cycleIDs[cycle]}"}
            }
        } 

        # Make the request
        response = requests.post(self.queryUrl, headers=self.headers, json=data)

        if response.status_code == 200:  
            fellowsJson = response.json()
        else:  
            print(f"Request to get fellows failed with status code {response.status_code}")
            print(f"Response data: {response.text}")
            return 

        fellows = convertJsonToFellows(fellowsJson)

        return fellows
        

    def getTuteeApps(self, cycle : Cycle) -> List[TuteeApp]: 
        
        # Set parameters for request 
        data = {
            'dataCollectionId': "TuteeApplications",
            'query': {
                'filter': {'cycle': f"{self.cycleIDs[cycle]}"}
            }
        } 

        # Make the request
        response = requests.post(self.queryUrl, headers=self.headers, json=data)

        if response.status_code == 200:  
            tuteesJson = response.json()
        else:  
            print(f"Request to get tutees failed with status code {response.status_code}")
            print(f"Response data: {response.text}")
            return 

        tutees = convertJsonToTutees(tuteesJson)

        return tutees


    def postMatches(self, matches : List[Match]) -> bool: 
        return True


    def updateTutees(self, tutees : List[TuteeApp]) -> bool: 
        return True 


    def updateFellows(self, fellows : List[FellowApp]) -> bool: 
        return True

#######################################################
##               TESTING API CALLS                   ## 
#######################################################

requester = Requester()

# tutees = requester.getTuteeApps(cycle=Cycle.TEST)
    
# for tutee in tutees: 
#     print(tutee)

# fellows = requester.getFellowApps(cycle=Cycle.TEST)

# for fellow in fellows: 
#     print(fellow) 