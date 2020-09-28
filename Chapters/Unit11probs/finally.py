import sys

try:
    fout = open('blim.py', 'w')
    fout.write('import this')
except IOError, e:
    print "Error writing file: " + str(e)
finally:
    try:
        fout.close()
    except:
        pass
print "Continuing..."


