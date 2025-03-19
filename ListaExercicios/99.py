def potencia(n1, n2):
    return pow(n1,n2)

num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

pot = potencia(num1, num2)

print(f"\nA Potencia de ({num1},{num2}) é {pot}")