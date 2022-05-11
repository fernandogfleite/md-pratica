def euclides(dividendo, divisor):
    resto = dividendo % divisor

    if resto == 0:
        return divisor
    
    return euclides(divisor, resto)


numero_1 = int(input("N1: "))
numero_2 = int(input("N2: "))

mdc = euclides(numero_1, numero_2)

print(f"MDC({numero_1},{numero_2}) = {mdc}")