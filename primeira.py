from math import sqrt

num = int(input("Digite um número e verifique se ele é primo: "))

eh_primo = lambda number: not any(number%i==0 for i in range(2, int(sqrt(number))))

if eh_primo(num):
    print(f"{num} é um número primo")

else:
    print(f"{num} não é um número primo")
