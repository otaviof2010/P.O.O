'''
print ('QUESTÃO 1')
class pessoa:
    def __init__(self, nome, idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)
        print(f"{self.nome} agora tem {self.idade} anos.")

    def engordar(self, valorengordar):
        self.peso += valorengordar
        print(f"{self.nome} agora pesa {self.peso} kg.")

    def emagrecer(self, valoremagrecer):
        self.peso -= valoremagrecer
        print(f"{self.nome} agora pesa {self.peso} kg.")

    def crescer(self, valorcrescer):
        self.altura += valorcrescer
        print(f"{self.nome} agora mede {self.altura} cm.")

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
peso = float(input("Digite o peso da pessoa: "))
altura = float(input("Digite a altura da pessoa: "))

s = input("você engordou ou emagreceu? (Digite 'engordou' ou 'emagreceu'): ")
if s == 'engordou':
    valorengordar = float(input("Digite o valor para engordar a pessoa: "))
    valoremagrecer = 0
elif s == 'emagreceu':
    valoremagrecer = float(input("Digite o valor para emagrecer a pessoa: "))
    valorengordar = 0
else:
    print("Opção inválida. A pessoa não engordou nem emagreceu.")
    valorengordar = 0
    valoremagrecer = 0

v = input("você cresceu ou não cresceu? (Digite 'cresceu' ou 'não cresceu'): ")
if v == 'cresceu':
    valorcrescer = float(input("Digite o valor para crescer a pessoa: "))
else:
    valorcrescer = 0

envelhecer = input("você envelheceu? (Digite 'sim' ou 'não'): ")
if envelhecer == 'sim':
    envelhecer = True
else:
    envelhecer = False


pessoa1 = pessoa(nome, idade, peso, altura)
pessoa1.envelhecer()
pessoa1.engordar(valorengordar)
pessoa1.crescer(valorcrescer)


print ('QUESTÃO 2')

class conta:
    def __init__(self, numero, titular, saldo, limite, codigo_tipo, nome_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo
        self.nome_tipo = nome_tipo

    def deposita(self, valor):
        self.saldo += valor
        
    
    def saca(self, valor):
        if  valor <= self.saldo:
            self.saldo -= valor
            return True
        else:            
            return False
    
    
    def transferir(self, valor_transferencia, destino):
        if self.saca(valor_transferencia):
            destino.deposita(valor_transferencia)
            

        else:
            print("Saldo insuficiente para transferência.")

conta1 = conta(1, "João", 1000, 5000, 1, "Corrente")
conta2 = conta(2, "Maria", 2000, 5000, 2, "poupança")


voce = input("Deseja realizar uma transferência? (Digite 'sim' ou 'não'): ")
if voce == 'sim':
    valor_transferencia = int(input("Digite o valor para transferência: "))
    o = True
else:
    o = False
if o == True:
    m = input("Digite o número da conta de destino (1 para João ou 2 para Maria): ")

    if m == '1':
        destino = conta1
    elif m == '2':
        destino = conta2
    
    else:
        print("Número de conta inválido. A transferência não será realizada.")
        destino = None

if destino is not None:
    conta1.transferir(valor_transferencia, destino)
            


print(f"Saldo da conta de João: R${conta1.saldo}")
print(f"Saldo da conta de Maria: R${conta2.saldo}")

g = input("Deseja realizar outra coisa? (Digite 'sim' ou 'não'): ")
if g == 'sim':
    print('Opção para realizar outra coisa selecionada, oque deseja realizar? (1 para depósito, 2 para saque): ')
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        valor_deposito = float(input("Digite o valor para depósito: "))
        c = input("Digite o número da conta para depósito (1 para João ou 2 para Maria): ")
        if c == '1':
            conta1.deposita(valor_deposito)
        elif c == '2':
            conta2.deposita(valor_deposito)

        print(f"Saldo da conta de {conta1.titular} após depósito: R${conta1.saldo}")
    
    elif opcao == '2':
        valor_saque = float(input('digite um valor pra saque'))
        j = input('qual conta deseja efetuar o saque? (1 para joão, 2 para maria)')
        if j == '1':
            conta1.saca(valor_saque)
        elif j == '2':
            conta2.saca(valor_saque)
else:
    print ('operações encerradas')


print (conta1.saldo)
print (conta2.saldo)
'''