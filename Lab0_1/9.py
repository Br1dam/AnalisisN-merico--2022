def horn(lista,c):
    n = len(lista)
    res = lista[0]
    for i in range(1,n):
        res = res*c + lista[i]
    return res

p = horn([1,-5,6,2],2)
print(p)   

