# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric( p ):
    #Write your code here
    l = len( p )
    for i in p:
        if len( i ) != l:
            return False
    q = zip( *p )
    value = True
    for i in range( 0 , len( p ) ):
        for j in range( 0 , len( q ) ):
            if p[i][j] != ((-1)*q[i][j]):
                value = False
    return value


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
