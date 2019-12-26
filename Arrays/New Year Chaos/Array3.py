import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0

    for i in range(0, len(q)):
        if (q[i] - i) > 3:          # if a person swaps more than 2 positions
            print("Too chaotic")
            return

        for j in range(max(0, q[i]-2), i):      # bribes counter increased if a number that occurs on left of q[i] is greater than q[i]
            if q[j] > q[i]:
                bribes += 1



    print(bribes)
    return



if __name__ == '__main__':
    # minimumBribes([2, 5, 1, 3, 4])
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
