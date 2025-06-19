#!/usr/bin/python3
def add_tuple(a=(), b=()):
    l1 = list(a)
    l2 = list(b)
    if len(l1) < 2:
        z_list = [0 for _ in range(2 - len(l1))]
        l1 = l1 + z_list
    elif len(l1) > 2:
        l1 = l1[:2]
    i = 0
    while i < 2:
        l1[i] += l2[i]
        i = i + 1
    t = tuple(l1)
    return t
