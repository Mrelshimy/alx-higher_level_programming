#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    with requests.get('https://alx-intranet.hbtn.io/status') as res:
        print('Body response:')
        print(f'\t- type: {type(res.text)}')
        print(f"\t- content: {res.status_code}")
