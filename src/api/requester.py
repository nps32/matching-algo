import json
import requests
import boto3

from botocore.exceptions import ClientError
from typing import Dict, List

from src.models.enums.Cycle import Cycle
from src.models.enums.Grade import Grade
from src.models.enums.Subject import Subject
from src.models.enums.Day import Day

from src.models.tuteeApp import TuteeApp
from src.models.fellowApp import FellowApp
from src.models.match import Match

from src.utils.jsonConverters import (
    convertJsonToTutees,
    convertJsonToFellows,
    convertMatchesToJson,
    updateAppsJson
)


class Requester:
    """
    Handles API requests to Wix CMS for retrieving and updating application data.
    """

    def __init__(self):

        # URLs for Wix API Requests
        self.query_url = r'https://www.wixapis.com/wix-data/v2/items/query'
        self.bulk_insert_url = r'https://www.wixapis.com/wix-data/v2/bulk/items/insert'
        self.bulk_update_url = r'https://www.wixapis.com/wix-data/v2/bulk/items/update'

        # Extract authentication token from a local file
        with open('token.txt', 'r') as file:
            self.auth_token = file.read().strip()
        # TODO: replace when integrated with AWS Secrets Manager 
        # self.auth_token = self.get_secret()

        # Unique identifier for Hatch's Wix site
        self.site_id = 'fc608cb7-1555-4c42-b6b8-b3416ee6a801'

        # Construct required header for API calls 
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}',
            'wix-site-id': self.site_id
        }

        # Mapping cycle enums to Wix cycle IDs
        self.cycle_ids = {
            Cycle.TEST: "2bb261dd-2968-4c5b-bd05-731eaa7c3c87",
            Cycle.SPR24: "613958f3-cd19-4604-902b-4fffacf28672"
        }

    @staticmethod
    def get_secret():
        """
        Retrieves API key from AWS Secrets Manager.
        """
        
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager', region_name='eu-north-1')

        try:
            secret_response = client.get_secret_value(SecretId='prod/matchingLambda/wixKey')
        except ClientError as e:
            error_message = (
                f"ClientError occurred.\n"
                f"Error Code: {e.response['Error']['Code']}\n"
                f"Error Message: {e.response['Error']['Message']}\n"
                f"Request ID: {e.response['ResponseMetadata']['RequestId']}\n"
                f"HTTP Status Code: {e.response['ResponseMetadata']['HTTPStatusCode']}"
            )
            print(error_message) #TODO: Change to CloudWatch logging
            raise e

        return secret_response['SecretString']

    def get_fellow_apps(self, cycle: Cycle) -> List[FellowApp]:
        """
        Fetch Fellow applications from Wix CMS for a given cycle.
        """
        
        data = {
            'dataCollectionId': "FellowApplications",
            'query': {'filter': {'cycle': self.cycle_ids[cycle]}} # Send request for specific cycle 
        }

        response = requests.post(self.query_url, headers=self.headers, json=data)

        if response.status_code == 200:
            return convertJsonToFellows(response.json()) # Use util function to return a list of FellowApp objects
        else: 
            error_message = (
                f"Request to get Fellow Apps failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}"
            )
            raise RuntimeError(error_message)

    def get_tutee_apps(self, cycle: Cycle) -> List[TuteeApp]:
        """
        Fetch Tutee applications from Wix CMS for a given cycle.
        """

        data = {
            'dataCollectionId': "TuteeApplications",
            'query': {'filter': {'cycle': self.cycle_ids[cycle]}} # Send request for specific cycle 
        }

        response = requests.post(self.query_url, headers=self.headers, json=data)

        if response.status_code == 200:
            return convertJsonToTutees(response.json()) # Use util function to return a list of TuteeApp objects
        else:
            error_message = (
                f"Request to get Tutee Apps failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}"
            )
            raise RuntimeError(error_message)

    def post_matches(self, matches: List[Match]) -> bool:
        """
        Post match data to Wix CMS.
        """

        data = {
            'dataCollectionId': 'Matches',
            'returnEntity': True,
            'dataItems': convertMatchesToJson(matches) # Use util function to translate match objects to proper JSON format
        }

        response = requests.post(self.bulk_insert_url, headers=self.headers, json=data)

        if response.status_code == 200:
            return True
        else: 
            error_message = (
                f"Request to post Matches failed.\n"
                f"Status Code: {response.status_code}\n"
                f"Response Data: {response.text}"
            )
            raise RuntimeError(error_message)

    def update_tutees(self, tutees: List[TuteeApp], cycle: Cycle) -> bool:
        """
        Update tutee data in Wix CMS.
        """

        query_data = {
            'dataCollectionId': "TuteeApplications",
            'query': {'filter': {'cycle': self.cycle_ids[cycle]}}
        }

        query_response = requests.post(self.query_url, headers=self.headers, json=query_data)

        if query_response.status_code != 200:
            error_message = (
                f"Request to get Tutee Apps for update failed.\n"
                f"Status Code: {query_response.status_code}\n"
                f"Response Data: {query_response.text}"
            )
            raise RuntimeError(error_message)

        update_data = {
            'dataCollectionId': 'TuteeApplications',
            'returnEntity': True,
            'dataItems': updateAppsJson(apps=tutees, data=query_response.json())
        }

        update_response = requests.post(self.bulk_update_url, headers=self.headers, json=update_data)

        if update_response.status_code == 200:
            return True 
        else: 
            error_message = (
                f"Request to update Tutee Apps failed.\n"
                f"Status Code: {update_response.status_code}\n"
                f"Response Data: {update_response.text}"
            )
            raise RuntimeError(error_message)

    def update_fellows(self, fellows: List[FellowApp], cycle: Cycle) -> bool:
        """
        Update fellow capacity data in Wix CMS. 
        """

        query_data = {
            'dataCollectionId': "FellowApplications",
            'query': {'filter': {'cycle': self.cycle_ids[cycle]}}
        }

        query_response = requests.post(self.query_url, headers=self.headers, json=query_data)

        if query_response.status_code != 200:
            error_message = (
                f"Request to get Fellow Apps for update failed.\n"
                f"Status Code: {query_response.status_code}\n"
                f"Response Data: {query_response.text}"
            )
            raise RuntimeError(error_message)

        update_data = {
            'dataCollectionId': 'FellowApplications',
            'returnEntity': True,
            'dataItems': updateAppsJson(apps=fellows, data=query_response.json())
        }

        update_response = requests.post(self.bulk_update_url, headers=self.headers, json=update_data)

        if update_response.status_code == 200:
            return True
        else:
            error_message = (
                f"Request to update Fellow Apps failed.\n"
                f"Status Code: {update_response.status_code}\n"
                f"Response Data: {update_response.text}"
            )
            raise RuntimeError(error_message)