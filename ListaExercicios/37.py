while True:
    print('\n\033[;0;45m-=-=-=-=-=-=-=-=-=-=- Reajusto de Salário -=-=-=-=-=-=-=-=-=-=-\033[m')

    nome = str(input('Nome do Funcionário: ')).casefold().title()
    anos_trab = int(input('Digite a quantos anos esta trabalhando na empresa: '))
    sal = float(input('Digite o salário atual: '))
    genero = str(input('Qual o genêro: ')).casefold()

    if genero == 'feminino':
        if anos_trab < 15:
            print(f'\nA funcionária {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.05}')
            print(f'O novo salário é de R$ {sal + (sal * 0.05):.2f}\n')
        elif anos_trab <= 20:
            print(f'\nA funcionária {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.12}')
            print(f'O novo salário é de R$ {sal + (sal * 0.12):.2f}\n')
        else:
            print(f'\nA funcionária {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.23}')
            print(f'O novo salário é de R$ {sal + (sal * 0.23):.2f}\n')  
    elif genero == 'masculino':
            if anos_trab < 20:
                print(f'\nO funcionário {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.03}')
                print(f'O novo salário é de R$ {sal + (sal * 0.05):.2f}\n')
            elif anos_trab <= 30:
                print(f'\nO funcionário {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.13}')
                print(f'O novo salário é de R$ {sal + (sal * 0.13):.2f}\n')
            else:
                print(f'\nO funcionário {nome} com {anos_trab} anos teve um reajuste de R$ {sal * 0.25}')
                print(f'O novo salário é de R$ {sal + (sal * 0.25):.2f}\n') 
    else:
        mensagem = f'Valor Inválido!'
        print(mensagem) 
        
    cont = str(input('\nDejesa Continuar: [S/N]')).casefold()
    if cont == 'n':
        print('Programa Encerrado!')
        break
    
     