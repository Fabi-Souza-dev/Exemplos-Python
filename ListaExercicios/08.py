def calSal (sal_mensal, horas_trab): # DEFINICAO DA FUNCAO
    por_hora = sal_mensal / horas_trab
    return por_hora

print("-=-=-=-=-=-=-=-=-= Calculo de salário -=-=-=-=-=-=-=-=-=")
sal_mensal = float(input("Digite seu salário mensal: "))
horas_trab = int(input("Horas trabalhada mensalmente: "))

salario_h = calSal(sal_mensal, horas_trab)

print(f"Ganha por hora R$ {salario_h:.4}")
