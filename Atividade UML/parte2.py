class Autor:
    def __init__(self,nome,nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    def get_nome(self):
        return self.__nome
    
class Livro:
    def __init__(self,titulo,ano, autores=None):
        self.titulo = titulo
        self.ano = ano
        self.__autores = autores if autores else []
    
    def get_titulo(self):
        return self.titulo
    
    def get_ano(self):
        return self.ano


class Biblioteca:
    def __init__(self,nome,endereço):
        self.__nome = nome
        self.__endereço = endereço
        self.__catalogo = []
    
    def adicionar_livro(self,livro):
        self.__catalogo.append(livro)

    def __iadd__(self, livro):
        self.adicionar_livro(livro)
        return self

    def __isub__(self, livro):
        if livro in self._catalogo:
            self.__catalogo.remove(livro)
        return self
    
    def buscar_por_titulo(self, titulo):
        for livro in self.__catalogo:
            if livro.get_titulo() == titulo:
                return livro
        return "livro n encontrado"
    
    def listar_livros(self):
        return self.__catalogo
            
    



a1 = Autor("Mr. Beast", "Estadunidense")
a2 = Autor("Otavio", "Brasileiro")

L1 = Livro("sonacirema", 2007, [a1])
L2 = Livro("americanos", 2010, [a2])

biblioteca = Biblioteca("Biblioteca Central", "Rua 7, 777")

biblioteca += L1
biblioteca += L2

print("Livros da biblioteca:")
for livro in biblioteca.listar_livros():
    print(f"{livro.get_titulo()} ({livro.get_ano()})")

encontrado = biblioteca.buscar_por_titulo("sonacirema")
if encontrado:
    print("Livro encontrado:", encontrado.get_titulo())


