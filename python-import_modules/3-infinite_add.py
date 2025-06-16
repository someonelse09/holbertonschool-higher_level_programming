#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    if count == 0:
        print(0)
    else:
        res = 0
        for i in range(count):
            res += int(argv[i])
        print(res)
