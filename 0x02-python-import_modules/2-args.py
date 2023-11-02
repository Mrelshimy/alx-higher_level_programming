#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    s = 's'
    if count == 1:
        s = ''
    if count == 0:
        print("0 arguments.")
    else:
        print("{} argumnent{}:".format(count, s))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
