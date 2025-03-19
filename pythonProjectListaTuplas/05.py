lista = ['Ana', 'Pedro', 'Carlos']

print(lista)
adicionar = str(input("Digite o nome do novo convidado: "))
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

lista.insert(posicao-1, adicionar)

print(f"Lista atualizada de convidados: {lista}")
