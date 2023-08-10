#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_cd = ord(char)
        if (ord('a') <= ord(char) <= ord('z')):
            char_cd -= 32
        print("{:c}".format(char_cd), end='')
    print()
