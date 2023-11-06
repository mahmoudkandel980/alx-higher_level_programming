#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for listEl in range(len(my_list)):
        if my_list[listEl] % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
