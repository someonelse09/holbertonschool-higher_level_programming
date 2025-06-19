#!/usr/bin/python3
def multiple_returns(sentence):
    l = []
    l.append(len(sentence))
    if len(sentence) == 0:
        l.append("None")
    else:
        l.append(sentence[0])
    return tuple(l)
