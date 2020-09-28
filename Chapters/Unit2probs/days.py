# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def leap( year ):
    if (year%100 == 0) and (year%400 != 0):
        return False
    elif year%4 == 0:
            return True
    else:
        return False
    
        
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    daysOfmonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    daysofleap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = year2 - year1
    j = month2 - month1 
    k = day2 - day1
    if day1 == day2 and month1 == month2:
        days = 366
        print days
        return days
    if i != 0:
        while year1 != year2:
            if leap( year1 ):
                days = days + 366
            else:
                days = days + 365
            year1 = year1 + 1
    if j != 0:
        while month1 != month2:
            if leap( year2 ):
                days = days + daysofleap[ month1-1 ]
            else:
                days = days + daysOfmonths[ month1-1 ]
            month1 = month1 + 1
    days = days + k
    print days
    return days
   


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
