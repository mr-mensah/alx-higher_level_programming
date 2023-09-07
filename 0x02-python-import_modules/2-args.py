#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    avglen = len(sys.argv) - 1
    if avglen == 0:
        print("0 arguments.")
    elif avglen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(avglen))
    for i in range(avglen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
