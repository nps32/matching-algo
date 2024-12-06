import json
import requests 

url = r'https://www.wixapis.com/wix-data/v2/collections/' 

# Read the token from the file
with open('token.txt', 'r') as file:
    authToken = file.read().strip() 

with open('site-id.txt','r') as file: 
    siteId = file.read().strip()

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'{authToken}',  # Replace with your actual token
    'wix-site-id': f'{siteId}'
}

params = {
    'query': json.dumps({
        'filter': '{"approvalStatus":"NeedsReview"}'
    })
}

# Make the GET request
response = requests.get(url+'FellowApplications', headers=headers, params=params)

# Check the response status code and print the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response data:", response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response data:", response.text)