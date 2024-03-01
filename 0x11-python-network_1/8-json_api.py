#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys

    if not sys.argv[1]:
        attr = ""
    else:
        attr = sys.argv[1]
        responce = requests.post("http://0.0.0.0:5000/search_user", data={'q': attr})
        resp_json = responce.json()
        try:
            if resp_json:
                print(f'[{resp_json.get("id")}] {resp_json.get("name")}')
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
