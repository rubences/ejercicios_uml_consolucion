class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def pintar(self):
        print(f"Pintando un {self.nombre} con radio {self.radio}")