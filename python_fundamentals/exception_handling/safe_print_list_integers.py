#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    index = 0
    count = 0

    while index < x:

        try:
            my_list[index]
            print("{:d}".format(my_list[index]), end="")
            index += 1
            count += 1
        except (ValueError, TypeError):
            index += 1
            continue
    print("")
    return count
