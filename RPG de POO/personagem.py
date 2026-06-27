
"""Módulo Personagem — Lab 2: Sobrecarga de operadores + rich."""


from Lab1.dado import rolar_todos_atributos

class Personagem:
    """Representa um herói genérico no mundo de Forja de Heróis."""

    def __init__(self, nome: str, rolar: bool = True):
        """Inicializa o personagem; se rolar=True gera atributos aleatórios."""
        self.nome = nome

        if rolar:
            atributos = rolar_todos_atributos()
            self.forca = atributos ["FOR"]
            self.destreza = atributos ["DES"]
            self.constituicao = atributos ["CON"]
            self.sabedoria = atributos ["SAB"]
            self.inteligencia = atributos ["INT"]
            self.carisma = atributos ["CAR"]

        else:
            self.forca = 0
            self.destreza = 0
            self.constituicao = 0
            self.sabedoria = 0
            self.inteligencia = 0
            self.carisma = 0

    def nivel_total(self) -> int:
        """Retorna a soma dos 6 atributos."""
        return (
            self.forca + self.destreza + self.constituicao
            + self.sabedoria + self.inteligencia + self.carisma
        )


    # TODO 2-B: implemente __str__
    # Deve retornar uma string legível, ex: "Arador (nível total: 73)"
    def __str__(self) -> str:
        return f'{self.nome} (nível total: {self.nivel_total()})'

    # __repr__ fornecido como exemplo:
    def __repr__(self) -> str:
        return f"Personagem('{self.nome}', rolar=False)"

    # TODO 2-C: implemente __eq__
    # Dois personagens são iguais se tiverem o mesmo nivel_total().
    def __eq__(self, other) -> bool:
        return self.nivel_total() == other.nivel_total()

    # __lt__ fornecido — permite sorted() automaticamente:
    def __lt__(self, other) -> bool:
        return self.nivel_total() < other.nivel_total()

    # exibir_ficha_rich já está implementada no scaffold — apenas chame!
    def exibir_ficha_rich(self) -> None:
        from rich.console import Console
        from rich.table import Table
        console = Console()
        tabela = Table(title=f"Ficha de {self.nome}")
        tabela.add_column("Atributo"); tabela.add_column("Valor", justify="right")
        for attr in ["forca","destreza","constituicao","sabedoria","inteligencia","carisma"]:
            tabela.add_row(attr.capitalize(), str(getattr(self, attr, 0)))
        console.print(tabela)