#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev_value = 0
    for c in reversed(roman_string):
        value = dict.get(c, 0)
        if value < prev_value:
            sum -= value
        else:
            sum += value
            prev_value = value
    return sum
