# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

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



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
