import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'junk.txt'

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ctr = 0
    temp = [0]*len(arr)     # creating an array of all zeroes but length equal to arr

    for idx, value in enumerate(arr):       # for faster retrieval of index of required integer
        temp[value - 1] = idx           # temp[] contains the index value of each consecutive number in its proper ascending order or in other words indexes of arr values become values in temp array


    for i in range(0, len(arr)):
        if arr[i] != i + 1:         # if a number is not on its right position in arr
            t = temp[i]         # retrieving the actual index position of i
            arr[i], arr[t] = i+1, arr[i]    # swapping the current number with correct number at i in arr
            temp[i], temp[arr[t]-1] = i, t  # swap the index positions (values) in temp array too
            ctr += 1

    print(ctr)
    return ctr

    # def minimumSwaps(arr):
    # ctr = 0
    # for i in range(0, len(arr)-1):
    # if arr[i] != i+1:
    # ctr += 1
    # actual_index = arr.index(i+1)
    # temp = arr[i]
    # arr[i] = arr[actual_index]
    # arr[actual_index] = temp
    #
    # return ctr



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
