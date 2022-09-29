import Ej1

def rbisc(fun, I,tol, mit):
    izq = I[0]
    der = I[1]
    e = der - izq
    hx = []  # Historial de puntos medios
    hf = []  # Historial de sus respectivos valores funcionales
    c = [hx, hf]
    if ((fun(izq) * fun(der)) > 0):
        print('No es posible en este intervalo')
        return 0
    for i in range(0, mit):
        e/=2
        r = izq + e
        hx.append(r)
        fun_r = fun(r)
        hf.append(fun_r)
        if ( abs(e) < tol or abs(fun(r)) < tol):
            return c
        if ((fun(izq) * fun(der)) < 0):
            der = r
        else:
            izq = r
        
    return c

#Defino el máximo de iteraciones y la tolerancia
mit = 100
tol = 1e-5


#Primera Raiz:
I1 = [4.5,6.1]
res1 = rbisc(Ej1.serie_seno,I1,tol,mit)
cant_it = len(res1[0])
r = res1[0][cant_it-1]

#Segunda raiz:
I2 = [3,4]
res2 = rbisc(Ej1.serie_seno,I2,tol,mit)
cant_it = len(res2[0])
g = res2[0][cant_it-1]

#Imprimo ambas raices
h = []
h.append(r)
h.append(g)
print("Primera Raíz:       Segunda Raíz:")
print(h)
print("Primera Raíz:")
print(res1)
print("Segunda Raíz:")
print(res2)
