def ap(a):  #this procedure adds the "s" or not
    if a != 1:
        return "s"
    return ""

def convert_seconds(number):
    secs = number % 60.0
    if secs % 1 == 0:
        secs = int(secs)
    mins = int(number/60 % 60.0)
    hrs = int(number/3600 % 60.0)
    return str(hrs) + " hour" + ap(hrs) + ", " + str(mins) + " minute" + ap(mins) + ", " +  str(secs) + " second" + ap(secs)

def convert_bits(x,y):
    binary_values = [["kb",2**10*1.0],["kB",2**10*8.0],["Mb",2**20*1.0],["MB",2**20*8.0],["Gb",2**30*1.0],["GB",2**30*8.0],["Tb",2**40*1.0],["TB",2**40*8.0]]
    for a in binary_values:
        if y == a[0]:
            x = x * a[1]
    return x

def download_time(file_size,f_unit,bw_size,bw_unit):
    return convert_seconds(convert_bits(file_size,f_unit) / convert_bits(bw_size,bw_unit))
