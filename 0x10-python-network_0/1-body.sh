#!/bin/bash
# Sends a GET request to the URL and displays the body of the response for a 200 status code
curl -sX GET $1 -L
