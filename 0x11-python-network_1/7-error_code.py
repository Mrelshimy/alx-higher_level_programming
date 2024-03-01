#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys

    responce = requests.get(sys.argv[1])
    if responce.status_code < 400:
        print(responce.text)
    else:
        print(f'Error code: {responce.status_code}')
