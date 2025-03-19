def maior(n1, n2, n3):
    return n1, n2, n3

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

mr = max(maior(num1, num2, num3))

print(f"O maior número é {mr}")