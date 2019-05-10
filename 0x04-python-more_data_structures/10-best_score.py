#!/usr/bin/python3


def best_score(a_dictionary):
    try:
        mySortList = sorted(a_dictionary.items(), key = lambda kv: kv[1],
                            reverse = True)
        return(mySortList[0][0])
    except:
        return(None)
