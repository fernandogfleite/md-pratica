from math import sqrt
from collections import Counter

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


num1 = int(input("N1: "))
num2 = int(input("N2: "))

primos_n1 = fatores_primos(num1)
primos_n2 = fatores_primos(num2)

res_n1 = Counter(primos_n1)
res_n2 = Counter(primos_n2)

for number in res_n1.keys():
    if number not in res_n2.keys():
        res_n2[number] = 0


for number in res_n2.keys():
    if number not in res_n1.keys():
        res_n1[number] = 0


max_dict = dict()
min_dict = dict()

mmc = 1
mdc = 1

for number in res_n1.keys():
    min_num = min(res_n1[number], res_n2[number])
    max_num = max(res_n1[number], res_n2[number])

    max_dict[number] = max_num
    min_dict[number] = min_num

    mmc *= pow(number, max_num)
    mdc *= pow(number, min_num)


mmc_str = " x ".join([f"{num}^{exp}" for num, exp in sorted(max_dict.items())])
mdc_str = " x ".join([f"{num}^{exp}" for num, exp in sorted(min_dict.items())])

print(f"MDC({num1}, {num2}) = {mdc_str} = {mdc}")
print(f"MMC({num1}, {num2}) = {mmc_str} = {mmc}")