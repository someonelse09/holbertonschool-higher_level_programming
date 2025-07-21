#!/usr/bin/python3

i = 0
s = 1
while i < 9:
    print(i, end="")
    if i == 8:
        print("{}".format(s))
    else:
        print("{}".format(s), end=", ")

    s += 1
    if s > 9:
        i += 1
        s = i + 1
