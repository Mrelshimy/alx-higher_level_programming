#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    
    responce = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(responce.text)}')
    print(f"\t- content: {responce.status_code}")
