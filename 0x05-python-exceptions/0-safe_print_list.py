#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    my_list = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            my_list += 1
        except IndexError:
            break
    print("")
    return (my_list)
