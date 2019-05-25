#!/usr/bin/python3
"""
A function that a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    A function that a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if not isinstance(text, type("")):
        raise TypeError("text must be a string")

    line = ""
    i = 0
    while i < len(text):
        if any([text[i] is ".", text[i] is "?", text[i] is ":"]):
            line += text[i]
            line = line.strip()
            print(line, end='')
            print()
            print()
            line = ''
            i += 1
        else:
            line += text[i]
            i += 1
    if line != '':
        print(line.strip(), end='')
