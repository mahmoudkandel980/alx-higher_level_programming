#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = {}
    for element in a_dictionary:
        newDictionary[element] = a_dictionary[element] * 2
    return newDictionary
