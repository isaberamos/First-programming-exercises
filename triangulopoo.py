class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return(self.a + self.b + self.c)

    def tipo_lado(self):
        if (self.a == self.b) and (self.b == self.c) and (self.a == self.c):
            return("isósceles")
        elif (self.a == self.b) and (self.b == self.c):
            return ("equilátero")
        elif (self.a != self.b) and (self.b != self.c) and (self.c != self.a):
            return ("escaleno")

    def retangulo(self):
        retangulo = False
        if (self.a == self.c) and (self.b == self.d):
            return True


u = Triangulo(3,4,5)
print(u.retangulo())