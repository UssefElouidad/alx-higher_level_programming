#!/usr/bin/python3
"""
a Python script that takes GitHub credentials (username and password)
and uses the GitHub API to display id.

"""

import requests
import sys

# Extract username and personal access token from command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Set up the URL for the GitHub API endpoint to fetch user information
url = 'https://api.github.com/user'

# Set up the authentication using Basic Authentication with the provided username and personal access token
auth = (username, password)

# Send a GET request to the GitHub API endpoint with authentication
response = requests.get(url, auth=auth)

# Check if the response status code is successful (200)
if response.status_code == 200:
    # Parse the JSON response
    user_data = response.json()
    
    # Display the user id
    print("Your GitHub user id is:", user_data['id'])
else:
    # Display an error message if the request was not successful
    print("Failed to fetch user information. Error code:", response.status_code)
