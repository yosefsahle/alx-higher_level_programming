#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to
 the URL and displays the value of the variable
 X-Request-Id in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url_passed = sys.argv[1]

    req = requests.get(url_passed)
    print(req.headers.get("X-Request-Id"))
