#!/usr/bin/python3
def multiple_returns(sentence):
    result = []
    result.append(len(sentence))
    if len(sentence) == 0:
        result.append(None)
    else:
        result.append(sentence[0])
    return tuple(result)
