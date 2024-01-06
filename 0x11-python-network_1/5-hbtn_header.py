#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL and displays the value
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
