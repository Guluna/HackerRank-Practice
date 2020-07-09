#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:47:33 2020

@author: amnagul
"""


try:
     a = int(input('Enter a number: '))
     b = int(input('Enter another number: '))
     print(a/b)
     print('Okay')
     
except ValueError:
     print('String input cannot be converted to int.')
except ZeroDivisionError:
     print('Division by 0 not allowed')
except:
     print('Unknown Bug in user input.')

print('outside.')




print('fancy_divide function starts here ...')
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
print('Catching no error outputs: ')
fancy_divide([0, 2, 4], 1)
        
print('Index error outputs: ')
fancy_divide([0, 2, 4], 5)

print('Div by Zero error outputs: ')
fancy_divide([0, 2, 4], 0)

