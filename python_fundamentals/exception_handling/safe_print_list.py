#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    index = 0

    while index < x:

        try:
            my_list[index]
            print(my_list[index], end="")
            index += 1
        except IndexError:
            break
    print("\n")
    return index
