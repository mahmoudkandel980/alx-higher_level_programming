#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    return_value = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            return_value += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (return_value)
