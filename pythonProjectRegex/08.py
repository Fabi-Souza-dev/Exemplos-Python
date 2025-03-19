import re

cpf = input("Digite o CPF : ")

padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

if re.search(padrao, cpf):
    print("O CPF está no formato correto.")
else:
    print("CPF inválido")