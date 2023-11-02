#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1
    if counter == 0:
        print("{:d} argument.".format(counter))
        return
    else:
        if counter == 1:
            print("{:d} argument:".format(counter))
        else:
            print("{:d} arguments:".format(counter))
        i = 1
        while i <= counter:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
