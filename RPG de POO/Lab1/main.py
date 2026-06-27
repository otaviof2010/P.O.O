from Lab1.personagem import Personagem as p


def main():
    """Cria dois personagens e compara seus níveis."""
    heroi1 = p("Laylla")
    heroi2 = p("Otávio")
    heroi1.exibir_ficha()
    heroi2.exibir_ficha()
    if heroi1.nivel_total() > heroi2.nivel_total():
        print("Herói 1 possui um nível total maior que herói 2.")

    else:
        print("Herói 2 possui um nível total maior que herói 1.")
    # TODO 1-F: crie dois personagens com nomes da sua escolha,
    # exiba a ficha de cada um e mostre quem tem o maior nivel_total().
    # Exemplo:
    #   heroi1 = Personagem("Arador")
    #   heroi1.exibir_ficha()


if __name__ == "__main__":
    main()