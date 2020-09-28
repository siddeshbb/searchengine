#
# dish.py
#

class Dish(object):
    """
    Represents a food dish.
    """

    def __init__(self, name, price, description=None, vegetarian=False):
        self.name = name
        self.price = price
        self.description = description
        self.vegetarian = vegetarian
    
    def __str__(self):
        return "{name}{isveg}: {price:.2f}{desc}".format(
            name=self.name,
            desc=' (' + self.description + ')' if self.description else '',
            price=self.price,
            isveg='*' if self.vegetarian else '',
            extras = self.extras())
    def extras(self):
        pass
    
    
class MainDish(Dish): # you need to finish this
    """
    Represents an entree (main dish).
    """
    def __init__(self, name, price, description=None, vegetarian=False, sides=None):
        super(MainDish, self).__init__(name, price, description, vegetarian)
        self.sides = sides
        
    def __str__(self):
        return super(MainDish, self).__str__() + ' Sides: ' + str(self.sides)
        
        
class Appetizer(Dish): # you need to finish this
    """
    Represents an appetizer.
    """
    def __init__(self, name, price, description=None, vegetarian=False, serves=None):
        super(Appetizer, self).__init__(name, price, description, vegetarian)
        self.serves = serves
    
    def __str__(self):
        return super(Appetizer, self).__str__() + ' Serves: ' + str(self.serves)


