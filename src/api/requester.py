import json
import requests

from typing import Dict, List

from src.models.enums.Cycle import Cycle
from src.models.enums.Grade import Grade
from src.models.enums.Subject import Subject
from src.models.enums.Day import Day

from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp 
from src.models.match import Match

from src.utils.jsonConverters import convertJsonToTutees
from src.utils.jsonConverters import convertJsonToFellows
from src.utils.jsonConverters import convertMatchesToJson
from src.utils.jsonConverters import updateAppsJson


class Requester: 

    def __init__(self): 
        
        # URLs for Wix API Requests 
        self.queryUrl = r'https://www.wixapis.com/wix-data/v2/items/query'
        self.bulkInsertUrl = r'https://www.wixapis.com/wix-data/v2/bulk/items/insert'
        self.bulkUpdateUrl = r'https://www.wixapis.com/wix-data/v2/bulk/items/update'

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
            errorMessage = (
                f"Request to get Fellow Apps failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}\n"
                f"URL: {self.bulkInsertUrl}\n"
                f"Payload: {data}"
            )

            raise RuntimeError(errorMessage)

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
            print(f"Response data: {response.text}") 
            tuteesJson = response.json()
        else:  
            errorMessage = (
                f"Request to get Tutee Apps failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}\n"
                f"URL: {self.bulkInsertUrl}\n"
                f"Payload: {data}"
            )

            raise RuntimeError(errorMessage)

        tutees = convertJsonToTutees(tuteesJson)

        return tutees


    def postMatches(self, matches : List[Match]) -> bool: 

        # Set parameters for request 
        data = {
            'dataCollectionId': 'Matches',
            'returnEntity': True, 
            'dataItems': convertMatchesToJson(matches)
        } 

        response = requests.post(self.bulkInsertUrl, headers=self.headers, json=data) 

        if response.status_code == 200:  
            print(response.text)
            return True 
        else:  
            errorMessage = (
                f"Request to post Matches failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}\n"
                f"URL: {self.bulkInsertUrl}\n"
                f"Payload: {data}"
            )

            raise RuntimeError(errorMessage)


    def updateTutees(self, tutees : List[TuteeApp], cycle : Cycle) -> bool: 

        # Set parameters for request to get tutees current data in CMS 
        queryData = {
            'dataCollectionId': "TuteeApplications",
            'query': {
                'filter': {'cycle': f"{self.cycleIDs[cycle]}"}
            }
        } 

        # Make the request to get current tutees data in CMS 
        queryResponse = requests.post(self.queryUrl, headers=self.headers, json=queryData)

        # Ensure that initial API call was successful before proceeding 
        if queryResponse.status_code != 200:   
            errorMessage = (
                f"Request to post get Tutee Apps to update Tutee Apps failed.\n"
                f"Status Code: {queryResponse.status_code}\n"
                f"Response Data: {queryResponse.text}\n"
                f"URL: {self.bulkInsertUrl}\n"
                f"Payload: {queryData}"
            )

            raise RuntimeError(errorMessage)

        # Set parameters for request to update tutees data in CMS 
        updateData = {
            'dataCollectionId': 'TuteeApplications',
            'returnEntity': True, 
            'dataItems': updateAppsJson(apps=tutees, data=queryResponse.json())
        }  

        # Make the request to update tutees data in CMS 
        updateResponse = requests.post(self.bulkUpdateUrl, headers=self.headers, json=updateData)

        if updateResponse.status_code == 200:  
            return True 
        else:  
            errorMessage = (
                f"Request to update Tutee Apps failed.\n"
                f"Status Code: {updateResponse.status_code}\n"
                f"Response Data: {updateResponse.text}\n"
                f"URL: {updateResponse.bulkInsertUrl}\n"
                f"Payload: {updateData}"
            )

            raise RuntimeError(errorMessage)


    def updateFellows(self, fellows : List[FellowApp], cycle : Cycle) -> bool: 
         
        # Set parameters for request to get fellows current data in CMS 
        queryData = {
            'dataCollectionId': "FellowApplications",
            'query': {
                'filter': {'cycle': f"{self.cycleIDs[cycle]}"}
            }
        } 

        # Make the request to get current fellows data in CMS 
        queryResponse = requests.post(self.queryUrl, headers=self.headers, json=queryData)

        # Ensure that initial API call was successful before proceeding 
        if queryResponse.status_code != 200:   
             errorMessage = (
                f"Request to post get Fellow Apps to update Fellow Apps failed.\n"
                f"Status Code: {queryResponse.status_code}\n"
                f"Response Data: {queryResponse.text}\n"
                f"URL: {self.bulkInsertUrl}\n"
                f"Payload: {queryData}"
            )

        # Set parameters for request to update fellows data in CMS 
        updateData = {
            'dataCollectionId': 'FellowApplications',
            'returnEntity': True, 
            'dataItems': updateAppsJson(apps=fellows, data=queryResponse.json())
        }  

        # Make the request to update fellows data in CMS 
        updateResponse = requests.post(self.bulkUpdateUrl, headers=self.headers, json=updateData)

        if updateResponse.status_code == 200:  
            return True 
        else:  
            errorMessage = (
                f"Request to update Fellow Apps failed.\n"
                f"Status Code: {updateResponse.status_code}\n"
                f"Response Data: {updateResponse.text}\n"
                f"URL: {updateResponse.bulkInsertUrl}\n"
                f"Payload: {updateData}"
            )

            raise RuntimeError(errorMessage)


#######################################################################
##                        TESTING API CALLS                          ## 
#######################################################################

# requester = Requester()

# -------------------------Test 'getFellowApps'-------------------------
# fellows = requester.getFellowApps(cycle=Cycle.TEST)
# for fellow in fellows: 
#     print(fellow) 

# -------------------------Test 'getTuteeApps'-------------------------
# tutees = requester.getTuteeApps(cycle=Cycle.TEST)
# for tutee in tutees: 
#     print(tutee)

# -------------------------Test 'postMatches'-------------------------
# match1 = Match(tf_id='5d6b3e24-af54-4c23-b1e8-2f3ca0ec59f6', tutee_id=44, subject=Subject.CALC, grade=Grade.HE, cycle=Cycle.TEST)
# match2 = Match(tf_id='cd0cae6f-bf0c-4e05-84d7-25f0fb624c4a', tutee_id=101, subject=Subject.PHYSICS, grade=Grade.MI, cycle=Cycle.TEST)
# matches = [match1, match2]
# requester.postMatches(matches)

# -------------------------Test 'updateTutees'-------------------------
# tutee1 = TuteeApp(id='4af0bb98-69fd-49f0-82b2-67c174fa8714', cycle=Cycle.TEST, availability=[Day.MON, Day.WED], grade=Grade.MI, subject1=Subject.MATH2ALG, eval1=1, subject2=Subject.ACT_MATH, eval2=3, subject3=Subject.CHEM, eval3=4, match_count=5, capacity=10)
# tutee2 = TuteeApp(id='745badb9-4bc0-4c7a-8173-b6768c6d9fe2', cycle=Cycle.TEST, availability=[Day.MON, Day.WED], grade=Grade.MI, subject1=Subject.MATH2ALG, eval1=1, subject2=Subject.ACT_MATH, eval2=3, subject3=Subject.CHEM, eval3=4, match_count=10, capacity=10)
# tutees = [tutee1, tutee2]
# requester.updateTutees(tutees=tutees, cycle=Cycle.TEST)

# -------------------------Test 'updateFellows'-------------------------
# fellow1 = FellowApp(id='5d6b3e24-af54-4c23-b1e8-2f3ca0ec59f6', cycle=Cycle.TEST, availability = [Day.MON, Day.SAT, Day.FRI], grades=[Grade.MI, Grade.HS], subjects=[Subject.BIO, Subject.ACT_READ], match_count=10, capacity=10) 
# fellow2 = FellowApp(id='cd0cae6f-bf0c-4e05-84d7-25f0fb624c4a', cycle=Cycle.TEST, availability = [Day.MON, Day.SAT, Day.FRI], grades=[Grade.MI, Grade.HS], subjects=[Subject.BIO, Subject.ACT_READ], match_count=5, capacity=8) 
# fellows = [fellow1,fellow2]
# requester.updateFellows(fellows=fellows, cycle=Cycle.TEST)