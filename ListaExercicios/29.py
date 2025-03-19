print("-=-=-=-=-=-=-=-=- Reajuste Salária -=-=-=-=-=-=-=-=-")

while True:
    nome = str(input("Nome do Funcionário: "))
    sal = float(input("Salário R$: "))
    anos = int(input("A quantos anos está na empresa? "))

    if anos <= 3:
        print(f"O funcionário/a {nome}, com o reajuste de R$ {sal * 0.03} agora terá um novo salário de R$ {sal + (sal * 0.03)} ")
    elif 3 < anos <= 10:
        print(f"O funcionário/a {nome}, com o reajuste de R$ {sal * 0.125} agora terá um novo salário de R$ {sal + (sal * 0.125)} ")
    else:
        print(f"O funcionário/a {nome}, com o reajuste de R$ {sal * 0.20} agora terá um novo salário de R$ {sal + (sal * 0.20)} ")

    s = str(input("\nDseseja continuar? [S/N]")).strip().lower()
    if s == 'n':
        print("Encerrado...")
        break