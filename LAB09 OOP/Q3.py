from math import sqrt

class Rectangle: 
    def __init__(self, width = 1, length = 1):
        self.width = width
        self.length = length 
    def get_area(self):
        return (self.width * self.length)
    def __str__(self):
        return ('Rectangle: {} x {}'.format(self.width, self.length))
    
class EquilateralTriangle:
    def __init__(self, side_length = 1):
        self.side_length = side_length
    def get_area(self):
        return (sqrt(3) * self.side_length * (self.side_length/4))
    def __str__(self):
        return ('EquilateralTriangle({:.2f})'.format(self.get_area()))
    
class TriangularPrism:
    def __init__(self, side_length = 1, length = 10):
        self.side_length = side_length
        self.length = length
        self.base_triangle = EquilateralTriangle(side_length)
        self.rectangle = Rectangle(side_length, length)

    def get_surface_area(self):
        surface_area = (2 * self.base_triangle.get_area() + (3 * self.rectangle.get_area()))
        return round(surface_area, 3)
    
                

prism1 = TriangularPrism(2, 5)
print(prism1.get_surface_area())
prism2 = TriangularPrism(3, 10)
print(prism2.get_surface_area())
prism3 = TriangularPrism()
print(prism3.get_surface_area())