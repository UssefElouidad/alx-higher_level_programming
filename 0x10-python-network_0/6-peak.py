#!/usr/bin/python3
""" Finds Peak values """


def find_peak(list_of_integers):
    """Find the peak in a list of integers."""
    if not list_of_integers:
        return None

    def binary_search(a, lo, hi):
        """Recursive binary search for the peak."""
        if lo == hi:
            return lo
        mid = (lo + hi) // 2
        if a[mid] > a[mid + 1]:
            return binary_search(a, lo, mid)
        else:
            return binary_search(a, mid + 1, hi)

    return list_of_integers[binary_search(list_of_integers, 0, len(list_of_integers) - 1)]

