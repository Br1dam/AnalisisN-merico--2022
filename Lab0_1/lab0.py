import math

def nummayor():
    
    n = 1
    i = 1
    while math.isinf(n) == False :
         n = 2 ** i
         i = i + 1
         print(i)
         
 
    return n



       
print(nummayor())

