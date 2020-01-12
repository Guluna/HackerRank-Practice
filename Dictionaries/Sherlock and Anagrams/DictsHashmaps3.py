import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.

# Definition: Anagram of one word is another word that 1. has same length as former word 2. created with the same alphabets
# Algorithm: 1. Find all substrings in the given string 2. Check if 2 substring fulfill the criteria for anagram (i.e. same length & same alphabets)

def sherlockAndAnagrams(s):

    substrings_list = []
    for i in range(len(s)):     # finding all substrings in s
        for j in range(i+1, len(s)+1):
            substrings_list.append(s[i:j])      # e.g. for abba, ['a', 'ab', 'abb', 'abba', 'b', 'bb', 'bba', 'b', 'ba', 'a']

    for i in range(len(substrings_list)): # sorting all elements of list so that comparison of each element with another becomes easier in dictionary below
        substrings_list[i] = ''.join(sorted(substrings_list[i]))


    dict_substrings = {}    # finding anagram pairs i.e. where value for each item in dict is multiple of 2
    for item in substrings_list:
        if item in dict_substrings:
            dict_substrings[item] +=1
        else:
            dict_substrings[item] = 1

    z = 0
    for j in dict_substrings.values():
        if j >= 2:
            z += j*(j-1)        # actual formula is n(n-1)/2 but I am doing division by 2 part only once at end to save computations

    print(z//2)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)


