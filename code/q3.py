import sys
import math


def printBinary(n):
    for i in range(2**n):
        print(format(i, '#08b'))


def runsOf0s(n):
    if(n<=0):
        return 0
    return 2*runsOf0s(n-1) + math.ceil(2**(n-2))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        exit(0)
    n = int(sys.argv[1])

    # printBinary(n)
    print(runsOf0s(n))