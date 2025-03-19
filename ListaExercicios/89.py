'''     
    Está opção não passa parametros
'''

def gerador():
    print("Opções de Bordas")
    print('Borda 1 : +-------=======------+')
    print('Borda 2 : ~~~~~~~~:::::::~~~~~~~')
    print('Borda 3 : <<<<<<<<------->>>>>>>')
    bordas = int(input("\nDigite sua opção: "))
    
    if bordas == 1:
        print("\n+-------=======------+\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "+-------=======------+")
    elif bordas == 2:
        print("\n~~~~~~~~:::::::~~~~~~~\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "~~~~~~~~:::::::~~~~~~~")
    elif bordas == 3:
        print("\n<<<<<<<<------->>>>>>>\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "<<<<<<<<------->>>>>>>")
    else:
        print("Opção Inválida")    
    
gerador()

# ESTÁ OPÇÃO É PASSANDO UM PARAMETRO

def gerador(bordas): # O PARAMETRO NESTE CASO É (BORDAS)
    print("Opções de Bordas")
    print('Borda 1 : +-------=======------+')
    print('Borda 2 : ~~~~~~~~:::::::~~~~~~~')
    print('Borda 3 : <<<<<<<<------->>>>>>>')
    
    if bordas == 1:
        print("+-------=======------+\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "+-------=======------+")
    elif bordas == 2:
        print("~~~~~~~~:::::::~~~~~~~\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "~~~~~~~~:::::::~~~~~~~")
    elif bordas == 3:
        print("<<<<<<<<------->>>>>>>\n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "     Portugol Studio   \n"
              "<<<<<<<<------->>>>>>>")
    else:
        print("Opção Inválida")    

# Passando um argumento ao chamar a função
opcao = int(input("Digite sua opção: "))
gerador(opcao)
