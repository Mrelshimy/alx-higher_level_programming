#!/usr/bin/python3
"""Python script that posts email to a given url"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    params = {'email': sys.argv[2]}
    stringQuery = parse.urlencode(params)
    url = sys.argv[1] + '?' + stringQuery
    with request.urlopen(url) as res:
        print(res.read().decode('UTF-8'))
