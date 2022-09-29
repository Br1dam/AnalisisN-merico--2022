def horn(coefs, x):
    n = len(coefs)
    b = coefs[0]
    for idx in range(1, n):
        b = coefs[idx] + x*b
    
    return b

p = horn([1, -5, 6, 2], 2)
print(p)