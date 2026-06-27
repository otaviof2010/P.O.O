classDiagram

class LogMixin {
  +log(mensagem)
}

class Midia {
  <<abstract>>
  +titulo: str
  +reproduzir() str
}

class Musica {
  +artista: str
  +duracao: float
  +reproduzir() str
}

class Video {
  +resolucao: str
  +reproduzir() str
}

class PodcastExterno {
  +titulo: str
  +episodio: int
  +reproduzir() str
}

class Playlist {
  +itens: list
  +adicionar(midia)
  +reproduzir_tudo()
  +total_itens
}

class Usuario {
  +nome: str
  +playlist_ativa: Playlist
}

Midia <|-- Musica
Midia <|-- Video

Playlist --|> LogMixin

Playlist o-- Midia : contém
Usuario o-- Playlist : possui

PodcastExterno ..> Midia : duck typing