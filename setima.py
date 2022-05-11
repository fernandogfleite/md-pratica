def combinacao_linear(a,b):
    if b == 0:
        return (a, 1, 0)

    (d, xx, yy) = combinacao_linear(b, a % b)

    return (d, yy, xx - (a//b)*yy)

def inverso(s, t, contador, m):
    inv = s + (t*contador)
    
    if inv > 0 and inv < m:
        return inv

    return inverso(s, t, contador+1, m)


n = int(input("N:"))
m = int(input("M:"))

combinacao = combinacao_linear(n, m)

inv = inverso(combinacao[1], m, 0, m)

print(f"O inverso de {n} mod {m} é {inv}")

