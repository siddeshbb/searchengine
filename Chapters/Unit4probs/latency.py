# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction( t , d ):
    speed = ((( 0.0+d)*2)/t)*1000
    speed = speed / speed_of_light
    return speed
    



print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?
#It is an incorrect input as no particle in the universe can travel faster that the speed of light :-P
