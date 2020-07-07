#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:18:04 2020

@author: amnagul
"""

# =============================================================================
#Inefficient fibonacchi code (calculating already calculated values again & again)
# =============================================================================
#  def fibonacchi(n):
#      if n == 1:
#          return 1
#      elif n == 2:
#          return 2
#      else:
#          return fibonacchi(n-1) + fibonacchi(n-2)
#      
#  print(fibonacchi(7))
# =============================================================================
# =============================================================================
            
def fibonacchiEfficient(n, aDict):
    if n in aDict:      # Memoization
        return aDict[n]
    else:
        ans = fibonacchiEfficient(n-1, aDict) + fibonacchiEfficient(n-2, aDict)
        aDict[n] = ans
        return ans
        
        
aDict = {1:1, 2:2}

print(fibonacchiEfficient(7, aDict))