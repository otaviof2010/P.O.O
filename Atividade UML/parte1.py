class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

    def descrever(self):
        return f"Veiculo:{self.marca},{self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, ano, num_portas):
        super().__init__(marca, ano)
        self.num_portas = num_portas

    def descrever(self):
        return f"{super().descrever().replace('Veiculo', 'Carro')},{self.num_portas}"
        
class Carro_esportivo(Carro):
    def __init__(self, marca, ano, num_portas, velocidade_max):
        super().__init__(marca, ano, num_portas)
        self.velocidade_max = velocidade_max

    def descrever(self):
        return f" {super().descrever().replace('Carro','Carro Esportivo')},|máx:{self.velocidade_max} km/h "



v1 = Veiculo('fiat','2001')
print(v1.descrever())

c1 = Carro('fiat',2010,4)
print(c1.descrever())

ce1 = Carro_esportivo('uno',2000,4,70)
print(ce1.descrever())