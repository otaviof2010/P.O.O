import exercicio2 as e



f1 = e.Filme('star_wars', 2001, 4)
f2 = e.Filme('harry potter', 2000, 5)
f3 = e.Filme('diario de um banana',2010, 3)

p1 = e.Playlist("filmes legais")
p2 = e.Playlist('filmes Mais legais')

p1.adicionar_filmes(f1)
p2.adicionar_filmes(f2)

f1.dar_nota(4.5)

p1.mostrar()
p2.mostrar()

print (id(p1.filmes[0]))
print (id(p2.filmes[0]))

p1.remover_filme(f1)  #se eu fiz a 