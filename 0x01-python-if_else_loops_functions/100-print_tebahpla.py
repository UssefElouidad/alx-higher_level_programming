#!/usr/bin/python3
for a in range (ord('Z'), ord('A')  - 1, -1):
    if ((a +1) % 2 == 1):
        a += 32
    print("{:c}".format(a), end="")
  
