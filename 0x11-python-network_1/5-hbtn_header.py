#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys

    responce = requests.get(sys.argv[1])
    print(responce.headers.get('X-Request-Id'))
