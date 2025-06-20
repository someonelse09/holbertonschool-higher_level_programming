#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    maximum_val = float('-inf')
    maximum_key = ''
    for k, v in a_dictionary.items():
        if v > maximum_val:
            maximum_val = v
            maximum_key = k
    return maximum_key
