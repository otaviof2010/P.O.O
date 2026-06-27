

class conta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual da conta {self.numero}: R${self.saldo}")
    
    def saque(self, valor):
        if  valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual da conta {self.numero}: R${self.saldo}")

'''conta1 = conta()
conta1.numero = 1
conta2 = conta()
conta2.numero = 2
conta3 = conta()
conta3.numero = 3
conta1.deposito(1000)
conta1.saque(500)
conta2.deposito(2000)
conta2.saque(1500)
conta3.deposito(500)
conta3.saque(200)
'''