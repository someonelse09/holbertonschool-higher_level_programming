#!/usr/bin/python3
def add_tuple(a=(), b=()):
    l1 = list(a)
    l2 = list(b)
    if len(l1) > len(l2):
        z_list = [0 for _ in range(len(l1) - len(l2))]
        l2 = l2 + z_list
    elif len(l1) < len(l2):
        l2 = l2[:len(l1)]
    i = 0
    while i < len(l1):
        l1[i] += l2[i]
        i = i + 1
    t = tuple(l1)
    return t
