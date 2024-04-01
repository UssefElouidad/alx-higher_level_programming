#!/bin/bash

# a bash script that takes in a URL and displays the size of the body of the response

curl -sI "$1" | wc -c
