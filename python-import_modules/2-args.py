#!/usr/bin/python3
str = input()
argv = str.split()
if __name__ == "__main__":
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        print("1: {}".format(str))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i, argv[i]))
