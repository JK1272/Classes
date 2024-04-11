class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        return perimetro

    def calcular_area(self):
    
        s = self.calcular_perimetro() / 2  
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area


triangulo1 = Triangulo(lado1=3, lado2=4, lado3=5)

print("Perímetro do triângulo:", triangulo1.calcular_perimetro())
print("Área do triângulo:", triangulo1.calcular_area())