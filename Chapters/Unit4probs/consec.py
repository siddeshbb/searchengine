# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds( n ):
    if n == int( n ):
        h = n / 3600
        n = n - ( h * 3600 )
        m = n / 60
        n = n - ( m * 60 )
        if h == 1:
            hs = ' hour'
        else:
            hs = ' hours'
        if m == 1:
            ms = ' minute'
        else:
            ms = ' minutes'
        if n == 1:
            ns = ' second'
        else:
            ns = ' seconds'
        s = str( h ) + hs + ', ' + str( m ) + ms + ', ' + str( n ) + ns 
        return s
    else:
        p = int( n )
        q = p
        h = p / 3600
        p = p - ( h * 3600 )
        m = p / 60
        p = p - ( m * 60 )
        ad = n - q
        p = p + ad
        if h == 1:
            hs = ' hour'
        else:
            hs = ' hours'
        if m == 1:
            ms = ' minute'
        else:
            ms = ' minutes'
        s = str( h ) + hs + ', ' + str( m ) + ms + ', ' + str( p ) + ' seconds'
        return s


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
