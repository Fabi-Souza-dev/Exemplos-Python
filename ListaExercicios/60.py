homens30 = []
mulher18 = []
lista_idade = []

# Variáveis para armazenar a pessoa mais velha e a mulher mais jovem
nome_mais_velho = ''
idade_mais_velho = 0

nome_mulher_mais_jovem = ''
idade_mulher_mais_jovem = float('inf')

while True:
    print("\nCadastro de Pessoa:")
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    genero = input("Digite o gênero [M/F]: ").strip().upper()

    lista_idade.append(idade)

    # Verifica a pessoa mais velha
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome  

    # Verifica se é um homem e tem mais de 30 anos
    if genero == 'H' or genero == 'MASCULINO':
        if idade > 30:
            homens30.append(nome)  # Agora armazenamos o nome do homem

    # Verifica se é uma mulher e tem menos de 18 anos
    if genero == 'F' or genero == 'FEMININO':
        if idade < 18:
            mulher18.append(nome)  # Agora armazenamos o nome da mulher

        # Verifica a mulher mais jovem
        if idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade
            nome_mulher_mais_jovem = nome

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja cadastrar outra pessoa? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

# Cálculo da média das idades
media = sum(lista_idade) / len(lista_idade) if lista_idade else 0

# Exibição dos resultados finais
print("\n===== RESULTADO FINAL =====")
print(f"A pessoa mais velha é {nome_mais_velho}, com {idade_mais_velho} anos.")

if nome_mulher_mais_jovem:
    print(f"A mulher mais jovem é {nome_mulher_mais_jovem}, com {idade_mulher_mais_jovem} anos.")
else:
    print("Nenhuma mulher foi cadastrada.")

print(f"A média das idades é: {media:.2f}")
print(f"Homens com mais de 30 anos: {len(homens30)} ({', '.join(homens30)})")
print(f"Mulheres com menos de 18 anos: {len(mulher18)} ({', '.join(mulher18)})")
