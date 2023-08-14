#!/usr/bin/python3
import sys
n = len(sys.argv) - 1
if n == 0:
    print("{:d} arguments.".format(n))
elif n == 1:
    print("{:d} argument:".format(n))
    print("{:d}: {:s}".format(n, sys.argv[n]))
else:
    print ("{} argements:".format(n))
for x in range (1, n + 1):
    print("{:d}: {:s}".format(x, (sys.argv[x])))

