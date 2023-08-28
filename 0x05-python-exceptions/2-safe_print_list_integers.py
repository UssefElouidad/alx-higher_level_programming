#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while True:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
            if i == x:
                print()
                break
    except IndexError as e:
        print(e)
    finally:
        return count
