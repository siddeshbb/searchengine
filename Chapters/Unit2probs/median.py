# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median( a , b , c ):
    bigg = biggest(a, b, c)
    if bigg == a:
        big = bigger( b , c )
    elif bigg == b:
        big = bigger( a , c )
    else:
        big = bigger( a , b )
    return big







print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







