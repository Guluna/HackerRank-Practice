#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
No matter how long is a student's name, this code creates a new list with 
name of student and grades separated. If the student has no grades, append [] 
"""

data = [['Harry', 'Potter', 100],
        ['James', 'Bond', 7],
        ['Malala', 'Yusafzai'],
        ['Sherlock', 110],
        ['Martin', 'Luther', 'King']]

nameGrades = []

for i in data:
    try:
        name = i[:-1]
        grades = int(i[-1])
        nameGrades.append([name, [grades]])
    except ValueError:
        nameGrades.append([i[:], []])
        
print(nameGrades)

