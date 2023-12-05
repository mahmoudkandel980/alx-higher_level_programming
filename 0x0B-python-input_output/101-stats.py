#!/usr/bin/python3

"""
Module that reads stdin line by line and computes metrics
"""


def print_stats(size, code_status):
    """
    Prints statistics

    Args:
        size (int): The accumulated file size
        code_status (dict): The accumulated status codes

    Returns:
        None
    """
    print("File size: {}".format(size))
    for key in sorted(code_status):
        print("{}: {}".format(key, code_status[key]))

if __name__ == "__main__":
    import sys

    size = 0
    code_status = {}
    codes_valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for line in sys.stdin:
            if counter == 10:
                print_stats(size, code_status)
                counter = 1
            else:
                counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes_valid:
                    if code_status.get(line[-2], -1) == -1:
                        code_status[line[-2]] = 1
                    else:
                        code_status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, code_status)

    except KeyboardInterrupt:
        print_stats(size, code_status)
        raise
