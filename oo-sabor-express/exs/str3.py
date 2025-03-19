class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Atributo protegido

# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)
