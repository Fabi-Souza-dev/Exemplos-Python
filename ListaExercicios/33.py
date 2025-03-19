def aprovar_emprestimo():
    print("\033[0;0;41m-=-=-=-=-=-=-=-=-=-=-=-=-= Empréstimo -=-=-=-=-=-=-=-=-=-=-=-=-=\033[m")
    nome = str(input("\nNome do Cliente: "))
    casa = float(input("Valor do Imóvel: "))
    sal = float(input("Salário: "))
    anos_pagar = float(input("Em Quantos Anos Deseja Pagar? "))

    meses = anos_pagar * 12
    limite = sal * 0.30
    prest = casa / meses

    print(f"\nValor da prestação: R$ {prest:.2f}")
    if prest <= limite:
        print("Empréstimo APROVADO")
    else:
        print("Empréstimo NEGADO")

aprovar_emprestimo()




