#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    else:
        dictionryList = list(a_dictionary)
        firstEl = dictionryList[0]
        for key in dictionryList:
            if a_dictionary[firstEl] < a_dictionary[key]:
                firstEl = key
        return firstEl
