pessoas = []
pesos = []
print("[FEMININO / MASCULINO] \n")
for i in range(8):
    pessoa = str(input("Digite o Genêro: ")).casefold()
    peso = float(input("Digite o peso "))
    
    
    pessoas.append(pessoa)
    
    
quant_mulher = sum(1 for pessoa in pessoas if pessoa == 'feminino')
quant_homens = sum(1 for pessoa in pessoas if pessoa == 'masculino')


print(f"Quantidade de mulheres: {quant_mulher}")
print(f"Quantidade de homens: {quant_homens}")

''' 
mulheres = 0
homens_acima_100kg = 0
soma_peso_mulheres = 0
quantidade_mulheres = 0
maior_peso_homem = 0

for i in range(8):  # Loop para 8 pessoas
    print(f"\n=== Pessoa {i+1} ===")
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    peso = float(input("Digite o peso (Kg): "))

    if sexo == 'F':  
        mulheres += 1  # Conta mulheres cadastradas
        soma_peso_mulheres += peso  # Soma o peso das mulheres
        quantidade_mulheres += 1  # Conta quantas mulheres há

    elif sexo == 'M':  
        if peso > 100:
            homens_acima_100kg += 1  # Conta homens com mais de 100Kg
        if peso > maior_peso_homem:
            maior_peso_homem = peso  # Atualiza o maior peso entre os homens

# Cálculo da média de peso das mulheres
media_peso_mulheres = soma_peso_mulheres / quantidade_mulheres if quantidade_mulheres > 0 else 0

# Exibe os resultados
print("\n=== RESULTADO ===")
print(f"Quantidade de mulheres cadastradas: {mulheres}")
print(f"Quantidade de homens acima de 100Kg: {homens_acima_100kg}")
print(f"Média de peso entre as mulheres: {media_peso_mulheres:.2f} Kg")
print(f"Maior peso entre os homens: {maior_peso_homem} Kg")

'''
