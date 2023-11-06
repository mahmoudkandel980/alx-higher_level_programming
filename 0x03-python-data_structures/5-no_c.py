#!/usr/bin/python3

def no_c(my_string):

    newString = ""

    for j in my_string:
        if j == 'c' or j == "C":
            pass
        else:
            newString = newString + j
    return newString
