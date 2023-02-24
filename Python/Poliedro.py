
class Poliedro:
    def __init__(self, qtdVertice, qtdAresta, qtdFace, lado1, lado2, altura):
        self.qtdVertice = qtdVertice
        self.qtdAresta = qtdAresta
        self.qtdFace = qtdFace
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura
    
    def isConvex(self, qtdVertice, qtdAresta, qtdFace):
        if qtdVertice - qtdAresta + qtdFace == 2:
            return True
        else:
            return False
        
    def __str__(self):
        if self.isConvex == True:
            return f"O Poliedro É convexo Area:{self.calcArea} Volume:{self.calcVolume}"
        else:
            return f"O Poliedro NÃO é convexo Area:{self.calcArea} Volume:{self.calcVolume}"

class Cubo(Poliedro):
    def __init__(self, lado1):
        super().__init__(8, 12, 6, lado1, lado1, lado1)
    
    def calcArea(self):
        return 6 * self.lado1 ** 2
    
    def calcVolume(self):
        return self.lado1 ** 3
    
    def __str__(self):
        return f"O Poliedro é um Cubo Area:{self.calcArea()} Volume:{self.calcVolume()}"  
    
class Paralelepipedo(Poliedro):
    def __init__(self, lado1, lado2, altura):
        super().__init__(8, 12, 6, lado1, lado2, altura)
    
    def calcArea(self):     
        return 2 * (self.lado1 * self.lado2 + self.lado1 * self.altura + self.lado2 * self.altura)
    
    def calcVolume(self):
        return self.lado1 * self.lado2 * self.altura
    
    def __str__(self):
        return f"O Poliedro é um Paralelepipedo Area:{self.calcArea()} Volume:{self.calcVolume()}"
    
class Piramide(Poliedro):    
    def __init__(self, lado1, lado2, altura):
        super().__init__(5, 8, 5, lado1, lado2, altura)
    
    def calcArea(self):
        return self.lado1 * self.lado2 + 2 * self.lado1 * self.altura + 2 * self.lado2 * self.altura
    
    def calcVolume(self):
        return self.lado1 * self.lado2 * self.altura / 3
    
    def __str__(self):
        return f"O Poliedro é uma Piramide Area:{self.calcArea()} Volume:{self.calcVolume()}"
    
    

























