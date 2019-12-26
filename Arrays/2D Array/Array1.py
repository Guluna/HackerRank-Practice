import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = 'junk.txt'

# Complete the hourglassSum function below.
def hourglassSum(arr):
    my_list = []        # initializing list containing sum of each hour glass in given 6x6 2D array

    hourglass_up = 0
    hourglass_down = 0
    hourglass_mid = 0
    j = 0

    while(j <4):    # for looping via 0,1,2 rows then 1,2,3 rows then 2,3,4 then lastly 3,4,5 rows
        k, m, n = 0, 3, 1
        while(k<4 and m<7):     # for looping via 0,1,2 cols then 1,2,3 cols then 2,3,4 then lastly 3,4,5 cols
            for i in range(k,m):
                hourglass_up += arr[j][i]
                hourglass_mid = arr[j+1][n]
                hourglass_down += arr[j+2][i]


            my_list.append(hourglass_up+hourglass_down+hourglass_mid)
            k +=1; m+=1; n+=1
            hourglass_up = 0
            hourglass_down = 0
            hourglass_mid = 0
        j +=1


    # print(my_list)
    return max(my_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

