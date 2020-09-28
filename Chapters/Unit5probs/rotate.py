# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
def shift_n_letters(letter, n):
    o = ord(letter)
    i = 0
    if n < 0:
        while i > n:
            if o == ord('a'):
                o = ord('z')
            else:
                o = o - 1
            i = i - 1
    else:
        while i < n:
            if o == ord('z'):
                o = ord('a')
            else:
                o = o + 1
            i = i + 1
    return str(unichr(o))
    
def rotate(string,n):
    l = list(string)
    i = 0
    for i in range(0,len(string)):
        if l[i] == ' ':
            pass
        else:
            l[i] = shift_n_letters(l[i],n)
    return ''.join(l)

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
