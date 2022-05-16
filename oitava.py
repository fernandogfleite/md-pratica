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


a = int(input("A:"))
b = int(input("B:"))
m = int(input("M:"))

combinacao = combinacao_linear(a, m)

inv = inverso(combinacao[1], 0, m)

congruencia = b * inv

if congruencia > m:
    congruencia = congruencia % m

print(f"A solução para a congruência linear {a}x ≡ {b}mod({m}) é {congruencia}")

