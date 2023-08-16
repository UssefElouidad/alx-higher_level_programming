#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    not_uniq = set()

    for element in my_list:
        if element not in not_uniq:
            result += element
            not_uniq.add(element)
    return result
