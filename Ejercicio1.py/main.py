def main():
    figuras = [
        Circulo(5),
        Cuadrado(4),
        Triangulo(3, 6)
    ]

    for figura in figuras:
        figura.pintar()

if __name__ == "__main__":
    main()