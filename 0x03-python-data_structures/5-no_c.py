#!/usr/bin/python3


def no_c(my_string):
    copy_string = my_string[:]
    ch_list = list(copy_string)
    for i in range(len(ch_list)):
        if i < len(ch_list):
            if ch_list[i] == "c" or ch_list[i] == "C":
                del ch_list[i]
    new_string = ''.join(ch_list)
    return(new_string)
