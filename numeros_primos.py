# Escribir un programa para producir los primeros n números primos (2,3,5,7,...)

primos = []
n = 5
# contador: C
c = 2
while len(primos) < n:
    if c == 2:
        primos.append(c)
    else:
        aux = 0
        for primo in primos:
            if c % primo == 0:
                aux = 1
        if aux == 0:
            primos.append(c)
    c = c + 1

print(primos)