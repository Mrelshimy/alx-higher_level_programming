#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys
    attr = sys.argv[1] if len(sys.argv) > 1 else ""
    responce = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": attr})
    try:
        resp_json = responce.json()
        if resp_json:
            print(f"[{resp_json.get('id')}] {resp_json.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
