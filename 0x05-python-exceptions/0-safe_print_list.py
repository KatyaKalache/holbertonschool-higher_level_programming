def safe_print_list(my_list=[], x=0):
    if x >= 0:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print()
            return x
        except IndexError:
            pass
            print()
            return x-2
