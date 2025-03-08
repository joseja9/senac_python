import math

class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * (self.raio ** 2)

quadrado = Quadrado(4)
circulo = Circulo(3)

print(f'Área do quadrado: {quadrado.area():.2f}')
print(f'Área do círculo: {circulo.area():.2f}')
