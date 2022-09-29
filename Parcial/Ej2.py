import matplotlib.pyplot as plt
import Ej1

fig, ax = plt.subplots()

#Defino las listas hx y hy para luego graficar mi funcion
#para una lista de puntos separados por una distancia de 0,01

hx= []
hy = []
r = 0
s = 0

for i in range(0,640):
    r = r + 0.01
    hx.append(r)

for i in range(0,640):
    hy.append(Ej1.serie_seno(hx[i]))

plt.plot(hx,hy)



plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Defino el intervalo para el cual voy a graficar mi función

plt.xlim(0, 6.4)
plt.ylim(-1, 6.4)

plt.title("Aproximacion de la funcion seno por Pol. de Taylor, Primeros 5 términos")

plt.savefig("serie_seno.png")

plt.show() 