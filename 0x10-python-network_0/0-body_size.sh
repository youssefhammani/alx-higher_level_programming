#!/bin/bash
# Sends a request to the URL and displays the size of the response body in bytes

curl -sI $1 | grep "Content-Length" | cut -d " " -f2