#!/usr/bin/python3
def safe_print_integer(value):
    boole = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        boole = False
    return boole
