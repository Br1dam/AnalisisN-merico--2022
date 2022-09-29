import math

def mala(a,b,c):
    disc = b**2-4*a*c
    if disc <= 0:
        return ["Raiz negativa","Raiz negativa"]
    else:
        x_1=(-b-math.sqrt(disc))/2*a
        x_2=(-b+math.sqrt(disc))/2*a
        return[x_1,x_2]

def buena(a,b,c):
    disc = b**2-4*a*c
    if disc <= 0:
        return ["Raiz negativa","Raiz negativa"]
    else:
        if b > 0:
            x_1=(-b-math.sqrt(disc))/2*a
        else:
            x_1=(-b+math.sqrt(disc))/2*a
        x_2 = (c/a) / x_1
        return [x_1,x_2]

def main():
    a = float(input())
    b = float(input())
    c = float(input())
    resBuena = buena(a,b,c)
    print("Buena: ")
    for i in range(0,2):
        print(i+1,":",resBuena[i])
    resMala = buena(a,b,c)
    print("Mala: ")
    for i in range(0,2):
        print(i+1,":",resMala[i])

main()