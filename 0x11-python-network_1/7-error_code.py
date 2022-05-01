#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url_passed = sys.argv[1]
    req = requests.get(url_passed)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
