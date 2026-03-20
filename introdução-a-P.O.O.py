class amor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando que te ama.")
        print(f"{self.nome} tem {self.idade} anos.")

    def andar(self):
        print(f"{self.nome} está andando para te abraçar.")

nome = input("Digite o nome do seu amor: ")
idade = int(input("Digite a idade do seu amor: "))
nome1 = input("Digite o nome do seu amor: ")
idade1 = int(input("Digite a idade do seu amor: "))
nome2 = input("Digite o nome do seu amor: ")
idade2 = int(input("Digite a idade do seu amor: "))


self = amor(nome, idade)
self.falar()
self.andar()    
amor1 = amor(nome1, idade1)
amor1.falar()
amor1.andar()
amor2 = amor(nome2, idade2)
amor2.falar()
amor2.andar()

print(type(amor.amor1))