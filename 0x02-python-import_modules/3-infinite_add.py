#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    avglen = 0
    for i in range(len(sys.argv) - 1):
        avglen += int(sys.argv[i + 1])
    print("{}".format(avglen))
