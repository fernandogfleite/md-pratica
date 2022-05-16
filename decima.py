from copy import copy
from math import sqrt, gcd
from math import gcd


eh_primo = lambda number: not any(number%i==0 for i in range(2, int(sqrt(number))))

def combinacao_linear(a,b):
    if b == 0:
        return (a, 1, 0)

    (d, xx, yy) = combinacao_linear(b, a % b)

    return (d, yy, xx - (a//b)*yy)


def inverso(s, contador, m):
    inv = s + (m*contador)
    
    if inv > 0 and inv < m:
        return inv
    
    elif inv > m:
        return inv % m

    return inverso(s, contador+1, m)


congruencias = list()

M = 1
n = int(input("Digite a quantidade de congruências: "))

modulos = list()

for c in range(1, n+1):
    b = int(input(f"B{c}: "))
    m = int(input(f"M{c}: "))
    
    M *= m
    
    congruencias.append(
        {
            "b": b,
            "m": m
        }
    )
    
    modulos.append(m)
    
coprimos = True

for index, mod in enumerate(modulos):
    modulos_sem_mod = copy(modulos)
    modulos_sem_mod.pop(index)
    
    for modu in modulos_sem_mod:
        mdc = gcd(mod, modu)
        
        if mdc != 1:
            coprimos = False
            break
    
    if coprimos is False:
        break

    
x0 = 0

if coprimos is True:
    for congruencia in congruencias:
        a = M/congruencia["m"]
        m = congruencia["m"]
        b = congruencia["b"]
        
        combinacao = combinacao_linear(a, m)

        inv = inverso(combinacao[1], 0, m)

        if inv > m:
            inv = inv % m
        
        elif inv < 0:
            inv += m
        
        x0 += a * inv * b


    if x0 < 0:
        x0 += M

    elif x0 > M:
        x0 = x0 % M


    print(f"A solução única das {n} congruências é {int(x0)}")

else:
    print("Os módulos não são coprimos")