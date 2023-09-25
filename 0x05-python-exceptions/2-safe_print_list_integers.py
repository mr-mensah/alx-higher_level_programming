#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    a_count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            a_count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return a_count
