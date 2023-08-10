#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_cd = ord(char)
        if (ord('a') <= ord(char) <= ord('z')):
            char_cd -= 32
        print(chr(char_cd), end='')
    print()
