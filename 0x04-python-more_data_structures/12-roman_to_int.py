#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return(0)


    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
    sum = 0
    i = 0

    while (i < len(roman_string) and roman_string[i] in roman_numerals):
        first = roman_numerals[roman_string[i]]

        if (i + 1 < len(roman_string)):
            second = roman_numerals[roman_string[i + 1]]
            if first >= second:
                sum += first
                i += 1
            else:
                sum += second - first
                i += 2

        else:
            sum += first
            i += 1
    return(sum)
