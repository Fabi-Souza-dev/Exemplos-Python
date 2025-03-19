""" SAÍDA ESPERADA

    Aluno: João
    Idade: 16
    Nota: 8.5

    Aluno: Maria
    Idade: 17
    Nota: 9.2

    Aluno: Pedro
    Idade: 15
    Nota: 7.8

"""

dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados) - 2, 3):  # Garante que sempre há 3 elementos disponíveis
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])

    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")