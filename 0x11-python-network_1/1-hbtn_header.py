#!/usr/bin/python3
"""Python script that fetches value of 'X-Request-Id' header value"""

if __name__ == "__main__":
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers).get('X-Request-Id'))
