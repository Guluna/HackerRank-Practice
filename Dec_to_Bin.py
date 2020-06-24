# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

orig_num = -7
num = orig_num

if num <0:
    isNeg=True
    num = abs(num)
else:
    isNeg=False

result = ''

while num >0:
    result = str(num%2) + result
    num = num//2
    
if isNeg:
    result = '-'+result
    
print('Binary representation of {} is {}'.format(orig_num, result))