qtd_homens = []
qtd_mulheres = []
soma_idade = 0
mulheres_mais_20 = []
idade_homens = 0

print("\033[0;0;45m-=-=-=-=-=-=-=-=-=-=-=-=  Cadastro de Pessoas  -=-=-=-=-=-=-=-=-=-=-=-=\033[m")
for i in range(1,6):
    print(f"\nPessoa {i}")
    idade = int(input("Digite a idade: "))
    cadastro = str(input("Cadastre a pessoa: "))
    
    soma_idade += idade
    
    if cadastro == 'mulher':
        qtd_mulheres.append(cadastro)
        if idade > 20:
            mulheres_mais_20.append(idade) # para obter a qtd_mulheres acima de 20 anos
            
    elif cadastro == 'homem':
        qtd_homens.append(cadastro)
        idade_homens += idade
    else:
        print('Informação Inválida')
        
media = idade_homens / len(qtd_homens) if len(qtd_homens) > 0 else 0
print("\n\033[0;0;45m-=-=-=-=-=-=-=-=-=-=-=-=  Impressão de Cadastro de Pessoas  -=-=-=-=-=-=-=-=-=-=-=-=\033[m")       
print(f"\nQuantidade de Mulheres: {len(qtd_mulheres)}")
print(f"Quantidade de Homens: {len(qtd_homens)}")
print(f"A média da idade do grupo é {soma_idade / 5:.2f}")
print(f"A média da idade dos homen é {media}")
print(f"Quantidade de mulheres + de 20 anos: {len(mulheres_mais_20)}")
    
    
