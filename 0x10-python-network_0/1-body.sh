#!/bin/bash
# Sends a GET request to the URL and displays the body of the response for a 200 status code
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -w "200" && curl -sL "$1"
