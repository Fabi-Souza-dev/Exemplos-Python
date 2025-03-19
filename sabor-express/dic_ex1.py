pessoa = [{'nome':'Fafa dos Venenos', 'idade':'23', 'cidade':'Capivari'}]

# Atualização de Idade
pessoa['idade'] = 24

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']

# DICIONARIO COM NÚMEROS

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#  Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")
    
# Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)