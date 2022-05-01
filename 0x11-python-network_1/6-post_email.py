#!/usr/bin/python3
"""
script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url_passed = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url_passed, data=value)
    print(r.text)
