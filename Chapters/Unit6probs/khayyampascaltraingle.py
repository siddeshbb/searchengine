# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    l = []
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        i = 2
        l = [[],[1],[1,1]]
        while i < n:
            cur = [0] * (i+1)
            j = 0
            while j < i:
                if j == 0:
                    cur[j] = 1
                else:
                    cur[j] = l[i][j-1] + l[i][j]
                j = j + 1
            i = i + 1
            cur[-1] = 1
            l.append(cur)
        l.pop(0)
        return l
                    
            




#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
