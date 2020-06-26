#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

directly opening/creating and writing to a file

"""

handle_file = open('kids', 'w')

for i in range(2):
    name = input('Enter name: ')
    handle_file.write(name + '/')
    
    
handle_file.close()

"""

directly opening and reading from a file

"""
handle_file = open('kids', 'r')

for line in handle_file:
    print(line)
    
handle_file.close()