class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = self.altura * self.largura
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.altura + self.largura)
        return perimetro


retangulo1 = Retangulo(altura=5, largura=8)

print("Área do retângulo:", retangulo1.calcular_area())
print("Perímetro do retângulo:", retangulo1.calcular_perimetro())