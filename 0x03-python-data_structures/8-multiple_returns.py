#!/usr/bin/python3
def multiple_returns(sentence):
    sentenceLength = len(sentence)

    if (sentenceLength == 0):
        new_tuple = (sentenceLength, "None")
    else:
        new_tuple = (sentenceLength, sentence[0])
    return (new_tuple)
