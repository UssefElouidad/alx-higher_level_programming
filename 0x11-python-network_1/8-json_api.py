#!/usr/bin/python3
"""
 a Python script that takes in a letter
 and sends a POST request to http://0.0.0.0:5000/search_user
 with the letter as a parameter.

 """

import requests
import sys

# Get the letter from command line arguments or set it to an empty string if no argument is given
q = sys.argv[1] if len(sys.argv) > 1 else ""

# Make a POST request with the letter as a parameter
response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    # Parse response as JSON
    json_data = response.json()

    # Check if JSON is not empty
    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
except ValueError:
    # If response is not JSON formatted
    print("Not a valid JSON")
