#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    n = dir(hidden_4)
    for j in n:
        if j[:2] != '__':
            print("{:s}".format(j))

