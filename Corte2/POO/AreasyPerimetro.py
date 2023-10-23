####PARA UN CIRCULO####

class Circle:  
    pi = 3.14

    def __init__(self, diameter):  
        print('Crear un circulo con diametro: {d}'.format(d=diameter))
        self.radius = diameter / 2

    def area(self):  
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

circle = Circle(8)
circulo_area = circle.area()
print("El area del circulo es: ", circulo_area)
circulo_perimetro = circle.circumference()
print("El perimetro del circulo es: ",circulo_perimetro)

####PARA UN CUADRADO####

class Cuadrado:  

    def __init__(self, lado):  # Corregido el constructor
        print('Crear un cuadrado con lado: {l}'.format(l=lado))
        self.lado = lado

    def area(self):  # Corregido el método area
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

cuadrado = Cuadrado(8)
cuadrado_area = cuadrado.area()
print("El area del cuadrado es: ", cuadrado_area)
cuadrado_perimetro = cuadrado.perimetro()
print("El perimetro del cuadrado es: ",cuadrado_perimetro)

####PARA UN RECTANGULO####

class Rectangulo:

    def __init__(self, largo, ancho):
        print('Crear un rectangulo con largo: {l} y ancho: {a}'.format(l=largo, a=ancho))
        self.largo = largo
        self.ancho = ancho

    def area(self): 
        return self.largo * self.ancho

    def perimetro(self):
        return (self.largo * 2) + (self.ancho * 2)

rectangulo = Rectangulo(8,2)
rectangulo_area = rectangulo.area()
print("El area del rectangulo es: ", rectangulo_area)
rectangulo_perimetro = rectangulo.perimetro()
print("El perimetro del rectangulo es: ",rectangulo_perimetro)

####PARA UN TRIANGULO EQUILÁTERO####

class Triangulo: 

    def __init__(self, base, altura):
        print('Crear un triangulo rectangulo con base: {b} y altura: {a}'.format(b=base, a=altura))
        self.base = base
        self.altura = altura

    def area(self): 
        return (self.base * self.altura)/2

    def perimetro(self):
        return self.base*3

triangulo = Triangulo(8,3)
triangulo_area = triangulo.area()
print("El area del triangulo rectangulo es: ", triangulo_area)
perimetro_area = triangulo.perimetro()
print("El perimetro del triangulo rectangulo es: ",perimetro_area)

####PARA UN TRIANGULO ISOCELES####

class Triangulo: 

    def __init__(self, base, altura):
        print('Crear un triangulo isoceles con base: {b} y altura: {a}'.format(b=base, a=altura))
        self.base = base
        self.altura = altura

    def area(self): 
        return (self.base * self.altura)/2

    def perimetro(self):
        return ((((self.base/2)**2 + self.altura**2)**(1/2))*2)+self.base

triangulo = Triangulo(8,3)
triangulo_area = triangulo.area()
print("El area del triangulo isoceles es: ", triangulo_area)
perimetro_area = triangulo.perimetro()
print("El perimetro del triangulo isoceles es: ",perimetro_area)
