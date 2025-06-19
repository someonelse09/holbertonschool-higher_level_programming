#!/usr/bin/python3
def multiple_returns(sentence):
    l = []
    l.append(len(sentence))
    l.append(sentence[0])
    return tuple(l)
