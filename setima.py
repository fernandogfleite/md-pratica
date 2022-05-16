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


n = int(input("N:"))
m = int(input("M:"))

combinacao = combinacao_linear(n, m)
print(combinacao)

inv = inverso(combinacao[1], 0, m)

print(f"O inverso de {n} mod {m} é {inv}")

