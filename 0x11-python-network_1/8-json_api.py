#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys

    if not sys.argv[2]:
        attr = ""
    else:
        attr = sys.argv[2]
        responce = requests.post(sys.argv[1], data={'q', attr})
        resp_json = responce.json()
        try:
            if resp_json:
                print(f'[{resp_json.get("id")}] {resp_json.get("name")}')
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
