def eval(a, x):
        #  evalua una funcion polinomial, con coeficientes de mayor a menor
        c = a[0]
        for i in range(1,len(a)):
                c = c*x+ a[i]    
        return c
        
def der_fun(p):
        # derivada de una funcion polinomial, con coeficientes de mayor a menor
        b= []
        max = len(p)
        for i in range(0, max-1):
            c = p[i]*(max - i -1)
            b.append(c)
        return b

def sign(a):
    if(a< 0):
        return '-'
    else:
        return '+'
        
def abs(a):
        if(a<0):
            return a*(-1)
        else:
            return a

def rbisc(fun, I,tol, mit):
    izq = I[0]
    der = I[1]
    u = eval(fun,izq)
    v = eval(fun,der)
    e = der - izq
    hx = []
    hf = []
    c = [hx, hf]
    if (sign(u) == sign(v)):
        print('No es posible en este intervalo')
        return 0
    for k in range(1, mit+1):
        e/=2
        r = izq + e
        hx.append(r)

        w = eval(fun,r)
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

#metodo N E W T O N    
def r_newton(p, x_0, err, mit):

    c_0 = x_0
    hx = []
    hf = []
    r = [hx, hf]
    v = fun(c_0); dv = fun(c_0)
    if (abs(v) < err):
            return r

    for i in range(mit+1):
        if abs(dv) == 0:
            break
        c = c_0 - ( v/ dv  )
        v = fun(c_0); dv = fun(c_0)
        hx.append(c)
        hf.append(v)

        if (abs(v) < err or abs(c - c_0) < err or abs( (c - c_0)/c ) < err):
            return r   

        c_0 = c
    return r


def fun(x):
	return (2*x - 2)

err =1e-5
res = r_newton(fun,8,err,100)
print(res)
#p = [,0, 1/3, 3,-4] #coef de mayor a menor

#Polinomio taylor aprx a tan(x)-2x
#fun = [62/2835, 0,0.1259259259,0,0.1333333,0,0.33333333,0,-1]

#Polinomio x**2 - 3 = 0
#fun = [1,0,-3]

#I = [0.8, 2]
mit = 100
tol = 0.0000001
#res = r_newton(fun, 4, tol, mit)
#cant_it = len(res[0])
#r = res[0][cant_it-1]

#print(res, cant_it, r) 


def aprox_cubica(a):
    
    funcion = [1,0,-a]
    r = r_newton(funcion,5,tol,mit)
    return r

#a =  aprox_cubica(10)

#cant_it = len(a[0])
#r = a[0][cant_it-1]
#print(a, cant_it,r)
