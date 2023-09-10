#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_ans = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_ans.append(True)
        else:
            list_ans.append(False)
    return (list_ans)
