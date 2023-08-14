#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    total = sum(int(sys.argv[x]) for x in range(1, n + 1))
    print("{:d}".format(total))
