#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    previous = 0
    current = 1
    after = current
    for i in range( 1 , n ):
        after = current + previous
        previous = current
        current = after
        
        
    return after
    





print fibonacci(36)
#>>> 14930352
