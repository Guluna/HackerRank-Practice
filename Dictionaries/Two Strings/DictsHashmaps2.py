import math
import os
import random
import re
import sys

# os.environ['OUTPUT_PATH'] = 'junk.txt'
# Complete the twoStrings function below.

def twoStrings(s1, s2):

# need to use dictionaries (aka hashtables) for fast O(1) retrieval

    char_dict = dict()
    for i in s1:        # storing characters in s1 as keys of dictionary
        char_dict.update({i:1})


    for i in s2:
        if i in char_dict.keys():   # searching for characters in s2 inside char_dict
                print('YES')        # if even a single character matches, program returns YES on-spot
                return

    print('NO')
    return


# time-out on 3/7 test cases
    # s1 = sorted(s1)
    # s2 = sorted(s2)
    #
    # for i in s1:
    #     if i in s2:
    #         print('YES')
    #         return
    #
    # print('NO')
    # return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        # fptr.write(result + '\n')

    # fptr.close()