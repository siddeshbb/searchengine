# You should edit only this file and do not change restaurant.py
# change something here so that chez_bananas.is_yummy() returns True

from restaurant import Restaurant
def really_yummy():
    return True
# These are test cases

mcdowells = Restaurant("McDowell's Hamgurger Emporium")
mcdowells.is_yummy = really_yummy
mcdowells.is_yummy()

chez_bananas = Restaurant("Chez Bananas Crib of Contentment")
chez_bananas.is_yummy = really_yummy
chez_bananas.is_yummy()

#test case:
print "Test is:", chez_bananas.is_yummy() == True
