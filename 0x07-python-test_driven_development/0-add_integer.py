#!/usr/bin/python3
""" defines an integer addition function """
def add_integer(a, b=98):
    """ a and b must be integers or floats.
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    TypeError exception if a or b are not inegers or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return(a + b)
