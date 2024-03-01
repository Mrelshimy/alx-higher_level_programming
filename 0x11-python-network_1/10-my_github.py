#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    basic = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=basic)
    responce = r.json()
    print(responce.get("id"))
