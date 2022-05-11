from math import sqrt

eh_primo = lambda number: not any(number%i==0 for i in range(2, int(sqrt(number))))

def menor_fator_primo(number):
    for i in range(2, number+1):
        if eh_primo(i) and number % i == 0:
            return i


def fatores_primos(number):
    menor_primo = menor_fator_primo(number)

    resultado_div = number // menor_primo

    if resultado_div == 1:
        return [menor_primo]
    

    return [menor_primo, *fatores_primos(resultado_div)]




num = int(input("Digite um número e veja sua decomposição em fatores primos: "))

primos = fatores_primos(num)

for primo in primos:
    print(primo)
