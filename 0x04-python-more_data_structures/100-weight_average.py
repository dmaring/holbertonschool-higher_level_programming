#!/usr/bin/python3


def weight_average(my_list=[]):
    new_list = []
    sum_list = []
    if not my_list:
        return(0)
    # multiply each tuple index
    for i in range(len((my_list))):
        new_list.append(my_list[i][0] * my_list[i][1])

    sum = 0
    # add each product of above to the next
    for i in range(len(new_list)):
        sum += new_list[i]

    denom = 0
    # find denominator
    for i in range(len(my_list)):
        denom += my_list[i][1]

    return(sum / denom)
