# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greater( a, b):
    if a > b:
        return a
    else:
        return b
def greatest( p ):
    if len(p) == 0:
        
        return 0
    z = greater( p[0] , p[1] )
    return greater( z , p[2] )
        



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
