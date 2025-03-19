print("-=-=-=-=-=-=-=-=-= Conversor de Temperatura -=-=-=-=-=-=-=-=-=")

f = float(input("Digite os graus em Fah: "))

c = (f - 32) * 5/9

print(f"A temperatura em Fahrenhit {f}f para Celsius é {c :.3f}c ".format(f,c))
