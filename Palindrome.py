# -*- coding: utf-8 -*-


def toChars(s):
    """
    s: string that might include punctuation, spaces etc along with alphabets (both upper & lower case)
    
    return: a string of lowercase characters
    
    """
    s = s.lower()
    
    new_s = ''
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            new_s += i
            
    return new_s
    

def isPalindrome(s):
    """
    
    s: string of characters
    
    return: True or False dependending whether string is a palindrome or not 
    
    """
    
    # base case
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False
    
    
clean_string = toChars('Was it a car or a cat I saw?')
print(clean_string)
print(isPalindrome(clean_string))
    


    
    
    
    
    
    

