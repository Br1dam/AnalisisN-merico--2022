import math


def serie_seno(x):

    res = 0
    for i in range(0,5):
        res = res + (((-1)**i) * x**(2*i + 1)/math.factorial(2*i + 1))
    return res


#Otra forma de implementar la función

def fun_seno2(x):
 return x + ((-1) * x**(3)/math.factorial(3)) + (x**(5)/math.factorial(5)) + ((-1) * x**(7)/math.factorial(7)) + (x**(9)/math.factorial(9))

#Ejemplo

#res = fun_seno(1)
#res2 = fun_seno2(1)

#print(res)
#print(res2)