#!/usr/bin/python3
def uppercase(c):
    for letter in c:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = ord(letter) - 32
            letter = chr(letter)
        print("{}".format(letter), end='')
    print('')
