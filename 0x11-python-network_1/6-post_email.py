#!/usr/bin/python3
"""Python script that posts email to a given url"""

if __name__ == "__main__":
    import sys
    import requests

    param = {'email': sys.argv[2]}
    responce = requests.post(sys.argv[1], data=param)
    print(responce.text)
