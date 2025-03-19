
lista_idades = []
while True:
    print("\n-=-=-=-=-=-=-=-=-= Idade dos Alunos -=-=-=-=-=-=-=-=-=")
    for i in range(5):

        idade = int(input(f"Idade do Aluno {i} : "))        
        lista_idades.append(idade)
        

    cont = int(input("\nDigite 9999 para encerrar: "))
    if cont == 9999:
        print("\nPrograma Encerrado!")
        print(lista_idades)
        print(f"A média das idades é: {sum(lista_idades)/5}")
        break