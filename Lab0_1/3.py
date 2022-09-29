import math

def nummenor():
    i = 0
    m = 1
    while math.isinf(m) == False :
        m = m / 2
        i = i + 1
        print(i)
        if math.isinf(m) == True :
         break
    return m
    
def nummayor():
    i = 0
    m = 1
    while math.isinf(m) == False :
        m = m * 2
        i = i + 1
        print(i)
        if math.isinf(m) == True :
         break
    return m

print(nummenor())
