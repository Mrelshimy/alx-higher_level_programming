#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if nargs == 0:
        print("0 arguments.")
    elif nargs == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(nargs))
        for i in range(nargs):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
