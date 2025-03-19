# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print("-=-=-=-=-=-=-=-=-= Calculo para Pintar Parede -=-=-=-=-=-=-=-=-=")
alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura da parede: "))

lata_tinta = 80
galao_tinta = 25

area = alt * larg
pint = area / 6  # Calcula a quantidade total de tinta necessária em litros

latas_nece = math.ceil(pint / lata_tinta)   # Calcula o número de latas necessárias (arredonda para cima)

custo = latas_nece * lata_tinta

print(f"A area e de {area} há ser pintada")
print(f"Para pintar a area de {area} você ira precisar de {pint}l, seria uma {latas_nece} lata")
print(f"O valor total é de R$ {custo :.2f}")