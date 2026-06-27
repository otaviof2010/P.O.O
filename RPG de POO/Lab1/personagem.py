from Lab1.dado import rolar_todos_atributos

# TODO 1-C: importe rolar_todos_atributos do módulo dado
# Sintaxe: from dado import rolar_todos_atributos


class Personagem:
    """Representa um herói com 6 atributos numéricos (estilo D&D 5e)."""

    def _init_(self, nome: str, rolar: bool = True):
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

    def exibir_ficha(self) -> None:

        print("===",self.nome,"===")
        print(f"FOR: {self.forca}  DES: {self.destreza}  CON: {self.constituicao}")
        print(f"SAB: {self.sabedoria}  INT: {self.inteligencia}  CAR: {self.carisma}")
        print(f"Nível total: {self.nivel_total()}")
        # TODO 1-E: implemente usando print(). Não use rich aqui — isso é Lab 2.