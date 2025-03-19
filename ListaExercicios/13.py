nome = str(input("Digite seu nome: "))
genero = str(input("Digite seu genero: "))
alt = float(input("Digite sua altura: "))

if genero in 'Masculino':
    print(f"O peso ideal de {nome}, é de {(72.7*alt)-58 :.2f}")
elif genero in 'Feminino':
    print(f"O peso ideal de {nome}, é de {(62.1*alt)-44.7 :.2f}")
else:
    print(f"Inválido")
