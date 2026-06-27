class Filme:

    def __init__(self,titulo, ano, nota):
        self.titulo = titulo
        self.ano = ano
        self.nota = nota
        
        
    def dar_nota(self,nova_nota):
        
        if 0 <= nova_nota <= 5:
            self.nota = nova_nota  
        else:
            print('nota invalida')
    
f1 = Filme('star_wars', 2001, 4)
f2 = Filme('harry potter', 2000, 5)

class Playlist:
    def __init__(self,nome):
        self.nome = nome
        self.filme = []


    def adicionar_filmes(self,novo_filme):
        self.filme.append(novo_filme)


    def mostrar(self):
        for i in range(len(self.filme)):
            print(self.filme[i].titulo)
            print(self.filme[i].ano)
            print(self.filme[i].nota)

    def remover_filme(self,filme_remove):
        if filme_remove in self.filme:
            for x in range(len(self.filme)):
                del self.filme[x]
        else:
            print ('filme não está na lista')
    

        




            

    
