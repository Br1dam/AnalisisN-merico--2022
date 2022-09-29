#Utilizo la definicion de la función de Newton, pero quito la derivada. 
#Y cambio la función de iteración
def r_steffensen(fun, x_0, err, mit):

    c_0 = x_0
    hx = []
    hf = []
    r = [hx,hf]

    v = fun(c_0)
   

    for i in range(mit+1):
    
        c = c_0 - ( (fun(c_0)**2)/ (fun(c_0 + v) - v))
        v = fun(c_0)
        hx.append(c)
        hf.append(v)

        if (abs(v) < err) or (abs(c_0 - c) / abs(c)) < err:
            return r

        c_0 = c
    return r

