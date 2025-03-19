qtd_altura = []
qtd_90 = []
qtd_50 = []
menor_alt = []
maior_alt = []
maior_peso= []

for i in range(1,8):
    print(f"Pessoa {i}")
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    
    qtd_altura.append(altura)
    
    if peso > 90:
        qtd_90.append(peso)
    if peso < 50:
       qtd_50.append(peso)
       if altura < 1.6:
           menor_alt.append(altura)
    if altura >= 1.9:
        maior_alt.append(altura)
        if peso >= 100:
            maior_peso.append(peso)
           


media = sum(qtd_altura)/len(qtd_altura) if len(qtd_altura) > 0 else 0
print("\n\033[0;0;45m-=-=-=-=-=-=-=-=-=-=-=-=  Impressão de Cadastro de Pessoas  -=-=-=-=-=-=-=-=-=-=-=-=\033[m") 
print(f"\nA média da altura: {media}")
print(f"Quantidade de pessoas com mais de 90kg: {len(qtd_90)}")
print(f"Quantidade de pessoas com menos de 50kg e menos de 1.60m: {len(menor_alt)}")
print(f"Quantidade de pessoas com mais de 1.9m e pesam mais 100kg: {len(maior_alt)}")
