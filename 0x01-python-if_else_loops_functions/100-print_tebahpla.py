#!/usr/bin/python3
for a in range (ord('Z'), ord('A') - 1, -1):
    char = chr(a)
    print(f"{char.lower() if a % 2 == 0 else char.upper()}", end="")
