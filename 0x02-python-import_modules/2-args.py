#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_num = len(sys.argv)
    if argv_num == 1:
        print('{:d} argument.'.format(argv_num - 1))
    elif argv_num == 2:
        print('{:d} argument:\n{:d}:'.format(argv_num - 1, argv_num - 1),
              str(sys.argv[1]))
    elif argv_num > 2:
            print('{:d} arguments:'.format(argv_num - 1))
            for i in range(1, argv_num):
                print('{:d}: {:s}'.format(i, sys.argv[i]))
