#!/usr/bin/python3
for a in range (ord('Z'), ord('A') - 1, -1):
    output = ""
    char = chr(a)
    print(f"{char.lower() if a % 2 == 0 else char.upper()}", end="")
    output += "{}".format(char.lower()) if a % 2 == 0 else "{}".format(char.upper())

print("{}".format(output), end="")
  
