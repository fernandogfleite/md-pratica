def combinacao_linear(a,b):
    if b == 0:
        return (a, 1, 0)

    (d, xx, yy) = combinacao_linear(b, a % b)

    return (d, yy, xx - (a//b)*yy)

num1 = int(input("N1:"))
num2 = int(input("N2:"))

combinacao = combinacao_linear(num1, num2)

print(f"mdc({num1},{num2}) = {combinacao[1]} x {num1} + {combinacao[2]} x {num2} = {combinacao[0]}")