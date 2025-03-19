import re

dados = input("Digite o nome completo e o ano de nascimento do paciente: ")
padrao = r'(\w+) (\w+) - (\d{4})'
# aqui determinando o padrão, em qual ordem será

resultado = re.search(padrao,dados) # para encontrar esse padrão especificado

if resultado:
    primeiro_nome = resultado.group(1) # encontra a primeira parte
    sobrenome  = resultado.group(2) # encontra a segunda parte
    ano_nascimento = resultado.group(3) # encontra a terceira parte

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"ANo de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido")
