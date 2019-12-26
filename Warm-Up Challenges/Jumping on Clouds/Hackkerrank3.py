import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'junk.txt'

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    if len(c) == 2: # if given array consists of only 2 elements which by default are always normal clouds
        return 1

    jumps = 0
    i = 0
    while(i < len(c)-1):    # iterating only till 2nd last element
            if c[i+2] == 0:
                i = i + 2
                jumps += 1
                if (i + 1 == len(c) - 1):   # if i is 2nd last element e.g. [..., i, 0], then there is only 1 possibility because c[-1] is always 0 so we increase our jump counter and break the loop
                    jumps += 1
                    break

            else:
                i = i + 1
                jumps +=1


    print(jumps)
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
