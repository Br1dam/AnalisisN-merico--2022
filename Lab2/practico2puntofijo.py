def eval(a, x):
        #  evalua una funcion polinomial, con coeficientes de mayor a menor
        c = a[0]
        for i in range(1,len(a)):
                c = c*x+ a[i]    
        return c

def abs(a):
        if(a<0):
            return a*(-1)
        else:
            return a


def ripf(fun,x0,err,mit):
 v = eval(fun,x0)
 i = 0
 hx = [x0]
 while (i < mit):
         x = v
         if (abs(x - x0) < err):
                 return hx
         
         x0 = x
         v = eval(fun,x0)
         hx.append(x0)
         i = i + 1
         
 return hx

fun = [2,-3,-2]
error= 0.00001
mite = 5
a = ripf(fun,-2,error,mite)
print(a)