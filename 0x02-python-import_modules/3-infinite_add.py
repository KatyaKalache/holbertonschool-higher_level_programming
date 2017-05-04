#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_count = len(sys.argv)
    total = 0
    for i in range(1, argv_count):
        total = total + int(sys.argv[i])
    print(total)
