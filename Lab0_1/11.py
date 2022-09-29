def sonOrtogonales(lista1,lista2):
    son = True 
    if lista1[0] * lista2[0] + lista1[1] * lista2[1]==0:
        print(lista1[0] * lista2[0] + lista1[1] * lista2[1])
        son = True 
    else:
        print(lista1[0] * lista2[0] + lista1[1] * lista2[1])
        son = False
    return son
lista1 = [1, 1.1024074512658109]
lista2 = [-1, 1/lista1[1]]
if not sonOrtogonales(lista1,lista2):
    print("Algo salio mal")