#!/usr/bin/python3
def print_last_digit(number):
        last_d = abs(number) % 10
        return last_d
result = print_last_digit(number)
result += print_last_digit(number)
print(result)
