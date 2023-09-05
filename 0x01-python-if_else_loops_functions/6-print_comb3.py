#!/usr/bin/python3
for figure1 in range(0, 10):
    for figure2 in range(figure1 + 1, 10):
        if figure1 == 8 and figure2 == 9:
            print("{}{}".format(figure1, figure2))
        else:
            print("{}{}".format(figure1, figure2), end=", ")
