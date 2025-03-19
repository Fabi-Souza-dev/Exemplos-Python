produto1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
produto2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

nova_tuplas = produto1 + produto2

print("Estoque combinado: ")
print(nova_tuplas)