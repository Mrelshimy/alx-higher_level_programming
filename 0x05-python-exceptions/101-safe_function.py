#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return
