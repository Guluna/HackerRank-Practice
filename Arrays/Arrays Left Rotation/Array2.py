
import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH']= 'junk.txt'
# Complete the rotLeft function below.

def rotLeft(a, d):
    new_arr = []
    for i in range(0, d):       # copying the digits to be rotated in another array
        new_arr.append(a[i])

    k = d
    for j in range(0, len(a) - d):  # bringing all end digits to the front
        a[j] = a[k]
        k +=1

    m = 0
    for l in range(len(a)-d, len(a)):       # appending the rotated digits to the end of original array
        a[l] = new_arr[m]
        m += 1


    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
