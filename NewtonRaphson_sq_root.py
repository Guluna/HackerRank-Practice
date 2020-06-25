# -*- coding: utf-8 -*-
"""
Using Newton Raphson method to find square (or any other) root of a polynomial equation
"""


num = 24
epsilon = 0.01
guess = num/2.0
count = 0

while abs(guess**2 - num) >= epsilon:
    guess = guess - (guess**2 - num)/(2*guess)     # denom is derivative of actual polynomial e.g. x^2 - 24
    count += 1
    
print('Using Newton-Raphson method we found the square root of {} which is {}, in {} iterations.'.format(num,guess, count))
    

