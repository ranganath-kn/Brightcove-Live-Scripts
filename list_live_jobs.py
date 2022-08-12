import requests
import getpass
import json

# Input API Key
api_key = getpass.getpass("Enter the X-API-KEY: ")

# Request Endpoint
base_url = "https://api.bcovlive.io/v1/jobs"

# Print Base URL
print('\nRequest Endpoint: ',base_url)

# Request Header
headers = {'X-API-KEY': api_key,'content-type':'application/json', 'Accept':'application/json'}

# GET request to the endoint with headers
response = requests.get(base_url, headers=headers)

# Print Response Status Code with it's detail
print("\nResponse Status: ", response.status_code, response.reason)

# Print the response in JSON format
pretty_json = json.loads(response.text)
print ("\nResponse:\n",json.dumps(pretty_json, indent=2))