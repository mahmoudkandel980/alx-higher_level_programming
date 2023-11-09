#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    li = a_dictionary.keys()
    for el in sorted(sortList):
        print("{:s}: {}".format(el, a_dictionary[el]))
