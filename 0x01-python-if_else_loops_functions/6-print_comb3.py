#!/usr/bin/python3
for n in range(0, 10):
    for r in range(0, 10):
        if r > n and n != 8:
            print("{}{}".format(n, r), end=', ')
        elif r > n:
            print("{}{}".format(n, r))
