#!/usr/bin/python3
import sys

if __name__ == "__main__":
    syslen = len(sys.argv)
    if syslen == 1:
        print("0 arguments.")
    elif syslen == 2:
        print("1 argument:")
    elif syslen > 2:
        print("{} arguments:".format(len(sys.argv)))

    for num, element in enumerate(sys.argv):
        if num > 0:
            print("{}: {}".format(num, element))
