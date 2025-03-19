import re

texto = input("DIgite o título dos livros: ")
letra = input("Digite a letra inicial para pesquisa: ")

# re.findall() usa se, para encontrar todas as palavras que começam com a letra informada

palavras = re.findall(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)
# re.IGNORECASE serve para ignorar a maiúscula e minúscula

print(palavras)