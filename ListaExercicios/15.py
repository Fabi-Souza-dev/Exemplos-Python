
# salário bruto
def calSal (): # DEFINICAO DA FUNCAO
    print("-=-=-=-=-=-=-=-=-= Calculo de salário -=-=-=-=-=-=-=-=-=")
    nome = str(input("\nDigite o seu nome: "))
    horas_tra = float(input("Digite a quantidade de horas trabalhadas por mês: "))
    vl_por_hora = float(input("Digite o valor por horas trabalhadas: "))

    salario = horas_tra * vl_por_hora

    # quanto pagou ao INSS
    inss = salario * 0.08
    # quanto pagou ao sindicato
    sind = salario * 0.05
    # imposto de renda
    imp_renda = salario  * 0.11

    desc = inss + sind + imp_renda

    return nome, salario, desc, inss, sind, imp_renda

def impostos(nome, salario, desc, inss, sind, imp_renda):
    print(f"\n\n-=-=-=-=-=-=-=-=-= Calculo de salário do {nome} -=-=-=-=-=-=-=-=-=\n")
    print(f"\tO salario bruto é R$ {salario :.2f}")
    print(f"\tIR (11%) : R$ {imp_renda}")
    print(f"\tINSS (8%) : R$ {inss}")
    print(f"\tSindicato (5%) : R$ {sind}")
    print(f"\tSalário Liquido : R$ {salario - desc}")

nome, salario, desc, inss, sind, imp_renda = calSal()
impostos(nome, salario, desc, inss, sind, imp_renda)