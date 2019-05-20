#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            number = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            number = 0
        except TypeError:
            print("wrong type")
            number = 0
        except IndexError:
            print("out of range")
            number = 0
        finally:
            result.append(number)
    return(result)
