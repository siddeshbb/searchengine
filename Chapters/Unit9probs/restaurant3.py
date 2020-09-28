# Modify init so that all Restaurant instances have name, owner and chef attributes
class Restaurant(object):
    """
    Represents a place that serves food.
    """
    def __init__(self, name, owner, chef):
        self.name = name
        self.owner = owner
        self.chef = chef
        
    def is_yummy(self):
        """Returns True if this restaurant is yummy; otherwise, returns False."""
        return False
    
    def display(self):
        """Display the restaurant."""
        print self.name

