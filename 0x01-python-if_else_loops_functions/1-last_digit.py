#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_signed_digit(number):
    if number < 0:
        return -(-number % 10)
    else:
        return number % 10


l_d = last_signed_digit(number)
message = "Last digit of {:d} is {:d} and is"
if l_d > 5:
    print(f"{message} greater than 5".format(number, l_d))
elif l_d == 0:
    print(f"{message} 0".format(number, l_d))
else:
    print(f"{message} less than 6 and not 0".format(number, l_d))
