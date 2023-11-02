#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    nargs = len(sys.argv) - 1
    for i in range(nargs):
        total += int(sys.argv[i + 1])
    print(total)
