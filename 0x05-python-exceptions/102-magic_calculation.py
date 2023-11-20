#!/usr/bin/python3
def magic_calculation(a, b):
    return_value = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            return_value += a ** b / i
        except Exception:
            return_value = b + a
            break
    return return_value
