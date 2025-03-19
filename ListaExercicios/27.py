print("-=-=-=-=-=-=-=-=- Média -=-=-=-=-=-=-=-=-")
while True:
    nome = str(input("Nome do Aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media = (nota1 + nota2) / 2

    if media >= 7:
        print(f"\nO Aluno/a {nome}, foi Aprovado !!! \nCom a nota {media}")
    elif 5 <= media < 7:
        print(f"\nO Aluno/a {nome}, esta de Recuperação !!! \nCom a nota {media}")
    else:
        print(f"\nO Aluno/a {nome}, foi Reprovado !!! \nCom a nota {media}")

    s = input("\nDeseja continuar ? [S/N]").strip().lower()
    if s == 'n':
        print("Encerrado....")
        break
