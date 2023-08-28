#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        if isinstance(a, int) and isinstance(b, int):
            result = a / b
            return result
    except ZeroDivisionError:
        result = None
        return
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
