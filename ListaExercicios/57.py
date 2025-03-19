pagos_mulheres = []
pagos_homens = []

for i in range(4):
    sal = float(input("Digite o salario: "))
    genero = str(input("Digite o genero M/H :"))
    
    if genero == 'm' or genero == 'mulher':
        pagos_mulheres.append(sal)
    if genero == 'h' or genero == 'homem':
        pagos_homens.append(sal)

print(f"\nO total salário pagos a mulheres é: {sum(pagos_mulheres)}")
print(f"O total salário pagos a homens é: {sum(pagos_homens)}")
     