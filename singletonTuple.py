# -*- coding: utf-8 -*-
"""
Analyzing the components (int & strings) within a tuple
input: a tuple
return: a tuple
"""
def getData(aTuple):
    nums = ()
    words = ()
    
    for i in aTuple:
        # nums += (i[0])  # error: can only concatenate tuple ('not int') to a tuple
        nums += (i[0],)
        if i[1] not in words:
            # words += i[1]  # error: can only concatenate tuple (not "str") to tuple
            words += (i[1],)
            
    min_num = (min(nums))
    max_num = (max(nums))
    uniq_words = len(words)
    
    return (min_num, max_num, uniq_words)

print(getData(((1, 'Hello'), (2, 'people'), (1, 'Hi'), (4, 'Hello'))))