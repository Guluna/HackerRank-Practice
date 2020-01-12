#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    if len(magazine) < len(note):
            print('No')
            return

    else:
        magazine = sorted(magazine)
        note = sorted(note)
        l = []              # list containing matching elements
        for i in note:
            if i not in magazine:        # important: if even a single word in note is not in magazine, simply return. No need to iterate over rest of elements
                print('No')
                return
            else:
                magazine.remove(i)
                l.append(i)

        if len(l) == len(note):
            print('Yes')
            return
        else:
            print('No')
            return

# # Below mentioned code works on 20 test cases but gives time-out error on remaining 2 :(
#     if len(magazine) < len(note):
#         print('No')
#
#     else:
#         magazine = sorted(magazine)
#         note = sorted(note)
#         l = []
#         for i in note:
#             if i in magazine:
#                 magazine.remove(i)
#                 l.append(i)
#
#         if len(l) == len(note):
#             print('Yes')
#         else:
#             print('No')



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()  # list

    note = input().rstrip().split()     # list

    checkMagazine(magazine, note)


