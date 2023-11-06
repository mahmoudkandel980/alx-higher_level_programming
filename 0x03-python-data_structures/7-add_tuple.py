#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newTuple = ()
    tupleA = tuple_a + (0, 0)
    tupleB = tuple_b + (0, 0)
    newTuple = tupleA[0] + tupleB[0], tupleA[1] + tupleB[1]
    return newTuple
