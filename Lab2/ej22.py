import math




def sign(a):
    if(a < 0):
        return '-'
    else:
        return '+'

def rbisc(fun, I,tol, mit):
    izq = I[0]
    der = I[1]
    u = fun(izq)
    v = fun(der)
    e = der - izq
    hx = []
    hf = []
    c = [hx, hf]
    if (sign(fun(izq)) == fun(der)):
        print('No es posible en este intervalo')
        return 0
    for k in range(1, mit+1):
        e/=2
        r = izq + e
        hx.append(r)

        w = fun(r)
        hf.append(w)
        if ( abs(e) < tol or abs(w) < tol):
            print('error es minimo', abs(e), abs(w) )
            return c
        if (sign(w) != sign(u)):
            der = r
            v = w
        else:
            izq = r
            u = w
    return c

def fun1(x):
   return x ** 2 - 2

l = rbisc(fun1,[0,8],0.0001,1000)
cant_it = len(l[0])
r = l[0][cant_it-1]

print(l, cant_it, r) 