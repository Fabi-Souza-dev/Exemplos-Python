import re

receita = str(input("Digite a descrição: "))

numero = re.findall(r'\d+', receita)[0]

print(f"O número da receita é: {numero}")
