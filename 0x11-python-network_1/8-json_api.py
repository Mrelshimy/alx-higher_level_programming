#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data={"q": q})
    try:
        resp = r.json()
        if resp:
            print(f"[{resp.get('id')}] {resp.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
