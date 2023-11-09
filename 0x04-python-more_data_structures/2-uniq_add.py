#!/usr/bin/python3
def uniq_add(my_list=[]):
    summation = 0
    uniqueList = list(set(my_list))

    for i in uniqueList:
        summation += i
    return summation
