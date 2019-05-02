#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    for idx, num in enumerate(argv):
        if idx > 0:
            sum += int(num)

    print(sum)
