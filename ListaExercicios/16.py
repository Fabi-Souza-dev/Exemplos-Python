import math

print("-=-=-=-=-=-=-=-=-= Calculo para Pintar Parede -=-=-=-=-=-=-=-=-=")
alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura da parede: "))

lata_tinta = 80

area = alt * larg
pint = area / 3  # Calcula a quantidade total de tinta necessária em litros

latas_nece = math.ceil(pint / lata_tinta)   # Calcula o número de latas necessárias (arredonda para cima)

custo = latas_nece * lata_tinta

print(f"A area e de {area} há ser pintada")
print(f"Para pintar a area de {area} você ira precisar de {pint}l, seria uma {latas_nece} lata")
print(f"O valor total é de R$ {custo :.2f}")


