#!/usr/bin/python3
"""Python script that fetches a link and handles HTTPerror"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response_data:
            print(response_data.read().decode('UTF-8'))
    except error.HTTPError:
        print(f'Error code: {response_data.code}')
