# MERCHANT SOCK


# Input Format
# The first line contains an integer
# The second line contains space-separated integers describing the colors of the socks in the pile.


import os


# creates a txt file in current folder
os.environ['OUTPUT_PATH'] = 'junk.txt'


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_socks = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if ((ar[i] == ar[j]) & (ar[i] > 0) & (ar[j] > 0)):  # (ar[i] > 0) & (ar[j] > 0) help us skip elements that have already been paired i.e. -1
                ar[i], ar[j] = -1, -1
                pair_socks+= 1
    return pair_socks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))         # input() waits for user to type & converts it to string, rstrip() removes
    # whitespaces, split() splits that string into parts, map(fn, iter) returns a list

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

