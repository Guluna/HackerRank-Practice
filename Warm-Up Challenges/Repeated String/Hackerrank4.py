import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'junk.txt'

# Complete the repeatedString function below.
def repeatedString(s, n):
    str_len = len(s)
    repetitions = n//str_len    # finding out how many times is a string s repeated
    remainder = n%str_len

    total_a = 0
    for i in s:     # finding out how many times the letter 'a' occurs in single instance of string s
        if i == 'a':
            total_a += 1

    total_a = repetitions * total_a     # for s=aba & n=10, this would result in 3*2=6

    for i in range(0, remainder):       # for s=aba & n=10, remainder = 1 so total_a would increment by 1
        if s[i] == 'a':
            total_a += 1

    return total_a





if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()