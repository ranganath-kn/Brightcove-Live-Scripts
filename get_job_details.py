import requests
import getpass
import json

# Get Job ID and API Key as Input
job_id = input("Enter the Job ID: ")
api_key = getpass.getpass("Enter the X-API-KEY: ")

# Variable for the Path to Parse later with the Input Job ID
base_url = "https://api.bcovlive.io/v1/jobs/"

# Parse the Path to generate the Request Endpoint and print the Request Endpoint
path_parse = [base_url, job_id]
request_endpoint = ''.join(path_parse)
print('\nRequest Endpoint: ',request_endpoint)

# Request Headers which contains API Key 
headers = {'X-API-KEY': api_key,'content-type':'application/json', 'Accept':'application/json'}

# GET request to the endoint with headers
response = requests.get(request_endpoint, headers=headers)

# Print Response Status Code with it's detail
print("\nResponse Status: ", response.status_code, response.reason)

# Print the response in JSON format
pretty_json = json.loads(response.text)
print ("\nResponse:\n",json.dumps(pretty_json, indent=2))
