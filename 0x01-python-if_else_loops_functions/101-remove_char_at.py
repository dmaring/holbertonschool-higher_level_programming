def remove_char_at(str, n):
    mystr = ''
    for index, ele in enumerate(str):
        if index != n:
            mystr += ele
    return(mystr)
