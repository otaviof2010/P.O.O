from abc import ABC,abstractmethod


class LogMixin:
    def log(self, mensagem):
        print(f"[LOG] {mensagem}")



class Midia(ABC):
    def __init__(self,titulo):
        self.titulo = titulo
    
    @abstractmethod
    def reproduzir(self) -> str:
        pass

class Musica(Midia):
    def __init__(self, titulo,artista,duracao):
        super().__init__(titulo)
        self.duracao = duracao
        self.artista = artista

    def reproduzir(self):
        return f"Tocando música '{self.titulo}' de {self.artista} com duração de {self.duracao} minutos"


class Video(Midia):
    def __init__(self, titulo,resolucao):
        super().__init__(titulo)
        self.resolucao = resolucao
    
    def reproduzir(self):
        return f' Reproduzindo {self.titulo}, com resolução de {self.resolucao}'


class PodcastExterno:
    def __init__(self, titulo, episodio):
        self.titulo = titulo
        self.episodio = episodio

    def reproduzir(self):
        return f"Reproduzindo o podcast '{self.titulo}' Episódio {self.episodio}"
    
class Playlist(LogMixin):
    def __init__(self):
        self.itens = []

    def adicionar(self, midia):
        self.itens.append(midia)
        self.log(f"Item adicionado: {getattr(midia, 'titulo', 'sem título')}")

    def reproduzir_tudo(self):
        return [item.reproduzir() for item in self.itens]

    @property
    def total_itens(self):
        return len(self.itens)


m1 = Musica("samurai","djavan",  3.5)
v1 = Video("Brasil x Haiti melhores momentos", "1080p")
p1 = PodcastExterno("Podpa", 42)



playlist = Playlist()

playlist.adicionar(m1)
playlist.adicionar(v1)
playlist.adicionar(p1)

print(playlist.total_itens)
print(playlist.reproduzir_tudo())