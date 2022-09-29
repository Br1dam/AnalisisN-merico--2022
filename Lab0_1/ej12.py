import math

def prueba():
    r = 1
    fun= math.sqrt(r**2+1) - 1
    fun1= r**2 / (math.sqrt(r**2 + 1) + 1)
    

    for i in range(20):
        r = 8 ** -i
        print(f'f({r}) = {fun} , g({r}) = {fun1}')


prueba()
