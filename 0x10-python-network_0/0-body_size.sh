#!/bin/bash

# a bash script that takes in a URL and displays the size of the body of the response

# Get URL from command line argument
URL=$1

# Send request to the URL and store response body in a temporary file
response=$(curl -sI $URL | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the body in bytes
echo $response
