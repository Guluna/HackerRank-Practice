import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'junk.txt'

# used "Difference array - range update" approach https://www.geeksforgeeks.org/difference-array-range-update-query-o1/
# wrote code directly into main function to avoid time out error

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    arr = [0] * n

    for _ in range(m):
        a, b, k = map(int, input().rstrip().split())
        arr[a-1] += k       # adding k to first index i.e a

        if b < len(arr):
            arr[b] -= k     # subtracting k from element directly (right) adjacent of second index i.e. b

    max = sum = 0
    for i in arr:
        sum += i
        if max<sum:
            max = sum

    fptr.write(str(max) + '\n')

    fptr.close()


# Complete the arrayManipulation function below.
# def arrayManipulation(n, queries):
#     arr = [0]*n
#
#     for j in range(0, len(queries)):
#         i = queries[j][0]-1; arr[i] += queries[j][2]
#
#         k = queries[j][1]
#         if k >= len(arr):
#             continue
#         else:
#             arr[k] -= queries[j][2]
#
#
#
#     temp = [0]*n
#     for i in range(n):
#         for j in range(i+1):
#             temp[i] += arr[j]
#
#
#
#     print(max(temp))
#     return


# def arrayManipulation(n, queries):
#     arr = [0]*n
#
#     for j in range(0, len(queries)):
#         for i in range(queries[j][0]-1, queries[j][1]):
#             arr[i] += queries[j][2]
#
#     print(max(arr))
#     return max(arr)