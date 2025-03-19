import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Catina','categoria':'Italiano', 'ativo':False}]

def Exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ \n""")

def Exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Status do Restaurante')
    print('4. Sair\n')

def finalizar_app():
     #os.system('cls') # COMANDO IMPORTANDO PARA LIMPAR O TERMINAL
    Exibir_sub_titulo('Programa Finalizado')

def Opcao_invalida():
    print('Opção inválida!\n')
    Voltar_menu()

def Exibir_sub_titulo(texto):
    ''' Essa função exibe o título de cada opção no menu'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def Cadastrar_novo_restaurante():
    # docstring são comentários detalhados em cada função, para que qualquer outro programador seja capaz de entender fácil e rápido seu código
    ''' Essa função é responsável por cadastrar um novo restaurante

        Inputs
        - Nome do restaurante
        - Categoria
        
        Output:
        - Adiciona um novo restaurante a lista de restaurante
    
    '''
    Exibir_sub_titulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')    
    dados_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_restaurante) # append serve para adicionar valor na variavel restaurante(lista)
    print(f'\nO restaurante {nome_do_restaurante} com sucesso!\n')
    Voltar_menu()

def Voltar_menu():
    
    input('\nDigite qualquer teclado para voltar ao menu! \n')
    main()

def Listar_restaurante():
    ''' Essa função é responsável por lista os restaurante  

        For:
        - Está listando os nomes de restaurante de minha lista
        
        Argumentos:
        - Nome restaurante - recebe o dicionário com o parâmetro para impressão
        - Categoria - recebe o dicionário com o parâmetro para impressão
        - Ativo - recebe uma condição para se o restaurante afirma se está ou não ativo
        
    '''
    Exibir_sub_titulo('Listando os Restaurantes')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes: # o for esta listando os itens da lista
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # o ljust() serve para padronizar os espaços 
    Voltar_menu()

def Alternar_estado_restaurante():
    ''' Essa função é responsável por alterar o status do restaurante
    
        
    '''
    Exibir_sub_titulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    Voltar_menu()
        
def Escolher_opcao():
   # O try é para a verificação, ele vai verificar se a opção digitada é correspondente, caso não seja ele identifica e devolve como opção inválida
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            Cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            Listar_restaurante()
        elif opcao_escolhida == 3: 
            Alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            Opcao_invalida()
    except:
        Opcao_invalida()

def main():
    os.system('cls')
    Exibir_nome_do_programa()
    Exibir_opcoes()
    Escolher_opcao()

if __name__ == '__main__':
    main()