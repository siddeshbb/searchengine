# Fix this code to not raise an exception when the file is not writeable

try:
    with open('blim.py', 'w') as fout:
        fout.write('import this')
except:
    print 'Exception occured'
