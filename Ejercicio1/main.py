from figuras import Circulo, Cuadrado, Triangulo, Elipse

def main():
    figuras = [
        Circulo(5),
        Cuadrado(4),
        Triangulo(3, 6),
        Elipse(4, 6)
    ]

    for figura in figuras:
        figura.pintar()

if __name__ == "__main__":
    main()