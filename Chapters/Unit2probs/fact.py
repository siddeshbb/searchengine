# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial( n-1 )



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

