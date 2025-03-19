lista_idade = []
qtdHomens = []
idade_mulher = []
idade_homens = []

for i in range(4):
    print(f"\nPessoa {i}")
    idade = int(input("Digite a idade: "))
    genero = str(input("Digite o genero: ")).strip()
    
    lista_idade.append(idade)
    
    if genero == 'mulher' or genero == 'm':
        idade_mulher.append(idade)
        
    if genero == 'homem' or genero == 'h':
        qtdHomens.append(genero)
        idade_homens.append(idade)
        
media = sum(idade_homens)/len(idade_homens) if len(idade_homens) > 0 else 0       


print("\n-=-=-=-=-=-=-=-=--= Impressão de Cadastros -=-=-=-=-=-=-=-=--=")
print(f"A maior idade é: {max(lista_idade)}")
print(f"A quantidade de homens cadastrados: {len(qtdHomens)}") 
print(f"Idade da mulher mais jovem: {min(idade_mulher)}")
print(f"A média da idade dos homens: {media}")
    