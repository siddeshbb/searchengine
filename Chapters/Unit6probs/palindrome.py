# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    l = len(s)
    if l == 0 or l == 1:
        return True
    elif s[0] == s[l-1]:
        return is_palindrome( s[1:l-1] )
    else:
        return False
        
 
 
 
 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
