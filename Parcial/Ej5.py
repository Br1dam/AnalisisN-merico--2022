from matplotlib import pyplot
import Ej4,Ej1

#Primera Raiz:
res1 = Ej4.r_steffensen(Ej1.serie_seno,3,1e-5,100)
cant_it1 = len(res1[0])
r = res1[0][cant_it1-1]

#Segunda Raiz:
res2 = Ej4.r_steffensen(Ej1.serie_seno,6,1e-5,100)
cant_it2 = len(res2[0])
q = res2[0][cant_it2-1]

#Imprimo ambas raices
print("Primera Raíz: ")
print(r)
print(cant_it1,"iteraciones requeridas")
print("Segunda Raíz: ")
print(q)
print(cant_it2,"iteraciones requeridas")

#Veamos que ocurre al iniciar la busqueda en 4.5

res3 = Ej4.r_steffensen(Ej1.serie_seno,4.5,1e-5,100)
cant_it3 = len(res3[0])
k = res3[0][cant_it3-1]

print("")
print("")
print("En el caso de que iniciemos la busqueda en 4.5 occure lo siguiente:")
print(k)
print(cant_it3,("iteraciones requeridas"))

#La funcion devuelve un valor distinto a las raices de la función, por lo que parece al iniciar en 4.5, no converge