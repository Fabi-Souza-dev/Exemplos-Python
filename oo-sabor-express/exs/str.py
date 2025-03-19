'''
    class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade
        
        
    # Criando 3 instâncias da classe Pessoa
    pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
    pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
    pessoa3 = Pessoa(nome='Jaque', idade=22)

    # Imprimindo informações iniciais
    print("Informações Iniciais:")
    print(pessoa1)
    print(pessoa2)
    print(pessoa3)
    print()

    # Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
    pessoa1.aniversario()
    pessoa3.aniversario()

    # Imprimindo informações após aniversário
    print("Informações após aniversário:")
    print(pessoa1)
    print(pessoa3)
    print()

    # Utilizando o método de classe saudacao para exibir mensagens personalizadas
    print(pessoa1.saudacao)
    print(pessoa2.saudacao)
    print(pessoa3.saudacao)

'''

# EX1

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular.title()
        self.saldo = saldo
        self._ativo = False
        
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"
    
    def ativar_conta(cls,conta):
       conta._ativo = True
    
    
conta1 = ContaBancaria('claúdia', 300)
conta2 = ContaBancaria('Rafael', 900)

print(f'Antes de ativar: Conta ativa? {conta1._ativo}')
print(conta2)
        
        
    
    
    