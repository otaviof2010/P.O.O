class Pessoa:
    def __init__(self,nome,idade,tamanho,genero):
        self.nome = nome
        self.idade = idade
        self.__tamanho = tamanho
        self.__genero = genero

    def get_tamanho(self):
        return self.__tamanho
    
    def set_tamanho(self,tamanho):
        self.__tamanho = tamanho

    def get_genero(self):
        return self.__genero

    def set_genero(self,genero):
        self.__genero = genero

    def envelhecer(self,cresce):
        self.idade += 1
        if self.idade < 21:
            self.__tamanho += cresce
    
    def crescer(self,cresce):
        self.__tamanho += cresce
    
    def printar_pessoa(self):
        print (f"nome: {self.nome}, idade: {self.idade}, tamanho: {n}, genero {m}")

p1 = Pessoa('Otávio',16,175,'masculino')
n = p1.get_tamanho()
m = p1.get_genero()
print (n,m)
k = p1.envelhecer(5)
g = p1.crescer(10)
n = p1.get_tamanho()
m = p1.get_genero()
print (n,m)

p1.printar_pessoa()
