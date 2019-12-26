#!/bin/python

# COUNTING # OF VALLEYS

import math
import os
os.environ['OUTPUT_PATH'] = 'junk.txt'

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    downs = 0
    ups = 0

    for j in s:
        if j == 'D':        # initial condition for valley
            downs -=1
        else:
            ups +=1
            if (downs + ups == 0):      # sea level reached
                valley +=1
                downs = 0
                ups = 0


    return valley



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(input())       # creating a list of U & D

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
