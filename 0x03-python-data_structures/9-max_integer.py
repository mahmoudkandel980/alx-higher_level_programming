#!/usr/bin/python3
def max_integer(my_list=[]):
    listLength = len(my_list)
    if listLength == 0:
        return "None"

    maxInteger = my_list[0]
    for i in range(1, listLength):
        if my_list[i] > maxInteger:
            maxInteger = my_list[i]
    return maxInteger
