base = input("Ingrese la base: ")
base = float(base)
potencia = 5

def potencia_enesima(base, potencia):

    i = 1
    fijo = base

    while i < potencia:
        base = base * fijo
        print(f"El valor es {base}")
        i = i+1

    return base

print(f"El valor es {base}")

potencia_enesima(base,potencia)