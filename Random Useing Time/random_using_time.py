import time
 
def tr1(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's numbers before the "."
    final = float(dem) * 10 # converts to a round number that is no more than 1 digit long
    z = int(final)
    return z
   
def tr2(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's numbers before the "."
    final = float(dem) * 100 # converts to a round number that is no more than 2 digits long
    z = int(final)
    return z
 
def tr3(x):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's numbers before the "."
    final = float(dem) * 1000 # converts to a round number that is no more than 3 digits long
    z = int(final)
    return z
 
def tr4(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's numbers before the "."
    temp = float(dem) * 10000000 # converts to a round number that is no more than 7 digits long
    final = temp / 192307.77 # makes sure that the result is not over 51
    z = int(final)
    return z
 
def tr5(x):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's the number before the "."
    temp = float(dem) * 10 # converts to a round number that is no more than 1 digit long
    temp2 = int(temp) + 1 # makes it a number form 1 to 10 and not 0 to 9
    final = temp2 * 1000 # gives a number between 1000 and 10000
    z = int(final)
    return z
 
def tr6(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's the number before the "."
    temp = float(dem) * 10 # converts to a round number that is no more than 1 digit long
    final = int(temp) + 1 # makes it a number form 1 to 10 and not 0 to 9
    z = int(final)
    return z
 
def tr7(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's the number before the "."
    temp = float(dem) * 10 # converts to a round number that is no more than 1 digit long
    final = int(temp) + 30 # makes it a number form 30 to 39 and not 0 to 9
    z = int(final)
    return z
 
def tr8(i):
    dis = time.time() # gets current time
    dem = dis-int(dis) # remove's the number before the "."
    temp = float(dem) * 10 # converts to a round number that is no more than 1 digit long
    final = int(temp) + 10 # makes it a number form 10 to 19 and not 0 to 9
    z = int(final)
    return z