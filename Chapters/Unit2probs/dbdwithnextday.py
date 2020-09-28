# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def datecheck( y1 , m1 , d1 , y2 , m2 , d2 ):
    if y1 < y2 :
        return True
    elif m1 < m2:
        return True
    elif d1 < d2:
        return True
    else:
        return False
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gergorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    days = 0
    while datecheck( year1 , month1 , day1 , year2 , month2 , day2 ):
        days = days + 1
        year1 , month1 , day1 = nextDay( year1 , month1 , day1 )
        
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
