# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list( p ):
    prod = 1
    for e in p:
        prod = prod * e
    return prod







print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
