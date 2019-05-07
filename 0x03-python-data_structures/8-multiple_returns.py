#!/usr/bin/python3


def multiple_returns(sentence):
    """A function that returns a tuple with the length of a string and its
    first character.
    """
    if sentence == '':
        first_char = None
        length = len(sentence)
    else:
        first_char = sentence[0]
        length = len(sentence)
    ret_tuple = (length, first_char)

    return(ret_tuple)
