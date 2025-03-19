def calcMULTA(): # FUNCAO CALCULADORA
    # CRIAR UM PROGRAMA QUE CALCULE O EXCESSO DE PESO, LIMITE MAX 50KG, CADA PESO A MAIS É 4 REAIS
    print("-=-=-=-=-=-=-=-=-= Calculadora Papo-de-Pescador -=-=-=-=-=-=-=-=-=")

    nome = str(input("Digite o nome do Pescador: "))
    dias_pes = int(input("Digite a quantidade de dias pescados: "))

    t_exc = 0
    t_multa = 0

    # GUARDAR O PESO A MAIS EM UMA VARIAVEL
    for i in range(dias_pes):  # O LOOP FOR IRÁ RODAR ATÉ QUE O VALOR PASSADO PELO USUARIO SEJA ATINGIDO
        kg = float(input(f"\nDigite a quantidade de peso pescado no {i + 1} dia: "))

        # GUARDAR A MULTA EM UMA VARIAVEL
        if kg > 50:
            kg_exc = kg - 50
            multa = kg_exc * 4
            t_exc += kg_exc  # FAZER AS VARIAVEIS QUE CRIEI PARA ARMAZERNAR O VALOR, RECEBER O VALOR DAS VARIAVEIS CORRESPONDENTE
            t_multa += multa  # FAZER AS VARIAVEIS QUE CRIEI PARA ARMAZERNAR O VALOR, RECEBER O VALOR DAS VARIAVEIS CORRESPONDENTE

    return t_exc, t_multa, nome

def imprimir(t_exc, t_multa, nome):
    print("\n\n-=-=-=-=-=-=-=-=-= Impressão do Valor Total -=-=-=-=-=-=-=-=-=")
    if t_exc > 0:
        print(f"\nO Pescador {nome} excedeu o limite de 50kg diário, passou {t_exc :.2f}kg a mais do permitido !")
        print(f"O valor da multa por excesso, é de R${t_multa :.2f}")
    else:
        print(f"\nParabéns, {nome}! Você não excedeu o limite de peso em nenhum dos dias.")

t_exc, t_multa, nome = calcMULTA()  # Recebe os valores calculados
imprimir(t_exc, t_multa, nome)  # Exibe os resultados

