# -*- coding: utf-8 -*-
"""
Finding Binary representation of a decimal number
"""

#x = float(input('Enter a decimal number between 0 & 1: '))
x=0.375

p=0
while (((2**p)*x)%1) != 0:      # converting fraction to whole num
    print('Remainder = ' + str(  (2**p)*x - int((2**p)*x) )  )
    p +=1
    
num = int(x * (2**p))
print('Whole number obtained after multiplying {} with  2^{} is: {}'.format(x, p, num))

result = ''

if num == 0:
    result = '0'
while num >0:
    result = str(num%2) + result
    num = num//2
    
print('The binary representation of whole number is: ', result)

for i in range(p - len(result)):
    result = '0' + result
    print(result)
    
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of decimal number {} is: {}'.format(x, result))
    
