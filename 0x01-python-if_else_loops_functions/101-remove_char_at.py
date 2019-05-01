def remove_char_at(str, n):
    mystr = ""
    for indx, ele in enumerate(str):
        if indx != n:
            mystr += ele
    return (mystr)
