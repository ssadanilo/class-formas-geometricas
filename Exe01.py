# Crie uma hierarquia de classes representando formas geométricas. Comece com uma classe base chamada
# "Forma" e, em seguida, crie classes derivadas como "Círculo" e "Retângulo"que herdem da classe base.
# Adicione métodos para calcular área e perímetro em cada classe derivada.

# Importando a função pi da biblioteca math
from math import pi

# Criando a classe base
class Forma:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

# Criando a classe derivada Círculo
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * pi * self.raio

# Criando a classe derivada Retângulo
class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)
    
# Uso das classes derivadas

circulo = Circulo(10)
print('Área do círculo:', circulo.calcular_area())
print('Perímetro do círculo:', circulo.calcular_perimetro())

retangulo = Retangulo(2, 4)
print('Área do retângulo:', retangulo.calcular_area())
print('Perímetro:', retangulo.calcular_perimetro())