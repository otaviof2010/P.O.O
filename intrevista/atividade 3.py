print ('ETAPA 1')

class Livro:     #cria a classe, e depois da as suas caracteristicas
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao



#instancia os objetos
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

#printa as caracteristicas do objeto
print(f"Título: {livro1.titulo}, Autor: {livro1.autor}, Ano: {livro1.ano_publicacao}")
print(f"Título: {livro2.titulo}, Autor: {livro2.autor}, Ano: {livro2.ano_publicacao}")

print ('ETAPA 2')
#diz que o livro novo está "olhando" e se "espelhando" na outra instancia
livro_novo = livro1

#muda o atributo de livro novo
livro_novo.ano_publicacao = 2000

#printa as caracteristicas do objeto mudado
print(f"Ano de publicação de livro1: {livro1.ano_publicacao}")
print(f"Ano de publicação de livro_novo: {livro_novo.ano_publicacao}")
#além de mudar em livro novo, o objeto de livro1 muda junto
print(f"ID de livro1: {id(livro1)}")
print(f"ID de livro_novo: {id(livro_novo)}")

print ('ETAPA 3')

    #cria uma função que automatiza o print, por exemplo se eu fizer, imprime_livro(livro2) ele vai mostrar todos os atributos como se fosse um print

def imprime_livro(livro):
    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")


#aqui eu faço a variavel olhar pra função, pra ela ser o apelido da função, automatizando ainda mais
  
funcao_impressao = imprime_livro

funcao_impressao(livro2)

#verifico o tipo dessa função
print(type(funcao_impressao))
#verifico se ocorre o mesmo com a função sem "apelido"
print(type(imprime_livro))

print ('ETAPA 4')

#implemento uma nova classe, com novos atributos
class Biblioteca:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []


    #uso o .append pra adicionar o livro na lista vazia de livros
    def adicionar_livro(self, livro):
        self.livros.append(livro)


    #lista os livros da lista, percorrendo a lista de livros, e utilizando a função ja feita de imprimir o livro, e como esta percorrendo a lista de livros, vai usando imprime livros no livro 1 e depois livro 2
    def listar_livros(self):
        print(f"Livros na biblioteca {self.nome}:")
        for i in range(len(self.livros)):
           imprime_livro(self.livros[i])
    
    #cria uma função pra encontrar o livro por titulo, onde, para cada livro na lista, eu quero saber se algum titulo dentro da lista, tem o mesmo titulo que eu pesquisei, e se tiver ele so printa o livro
    def encontrar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print('livro encontrado')
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")
                return livro
        print("Livro não encontrado")
        return None
    
    # mesma logica da função passada, so que removendo o livro no lugar de printar
    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return livro
                
# cria instancia
biblioteca = Biblioteca("Biblioteca Central")

# adiciona livros na biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

#chamo a função de listar os livros
biblioteca.listar_livros()

#chamo a função que retorna o livro
biblioteca.encontrar_livro_por_titulo('1984')


print ('ETAPA 5')

#troquei o primeiro elemento de autor da lista 
biblioteca.livros[0].autor = "Autor Desconhecido"

print(f"Autor de livro1: {livro1.autor}")
# modificou

#ID de cada um
print(f"ID de livro1: {id(livro1)}")
print(f"ID de biblioteca.livros[0]: {id(biblioteca.livros[0])}")
#ID iguais


print ('ETAPA 6')

# cria mais instancias
livro3 = Livro("A Revolução dos Bichos", "George Orwell", 1945)
livro4 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)

# adiciona os novos objetos a lista de livros da biblioteca
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

# remove o livro com esse titulo
biblioteca.remover_livro("1984")
biblioteca.listar_livros()


print(f"Título de livro2 após remoção: {livro2.titulo}")
# continuou