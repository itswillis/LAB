# define a constructor 
from math import sqrt 
class Hexagon:
    def __init__(self, side_length = 1):
         self.side_length = side_length

    def set_side_length(self, side_length):
        if side_length > 0: 
            self.side_length = side_length

    def get_side_length(self):
        return self.side_length
    
    def get_perimeter(self):
        self.perimeter = self.side_length * 6 
        return self.perimeter
    
    def get_area(self):
        self.area = (3*(sqrt(3))/2) * self.side_length * self.side_length
        return round(self.area, 2)

    ''' Note: The __str__ method should invoke self.get_area() to get the 
        area of a hexagon and invoke the self.get_perimeter() to get the perimeter of a hexagon and then display the result.'''

    def __repr__(self):
        return 'Hexagon({})'.format(self.side_length)
    
    def __str__(self):
        return 'A hexagon with an area of {:.2f} and a perimeter of {}.'.format(self.get_area(), self.get_perimeter())
    
    def __eq__(self, other):
        if not isinstance(other, Hexagon):
            return False
        return self.side_length == other.side_length
    
hexagon1 = Hexagon()
print(hexagon1)
hexagon2 = Hexagon(1)
print(hexagon2)
print(hexagon1 == hexagon2)

hexagon1 = Hexagon(10)
print(hexagon1)
hexagon2 = Hexagon(10)
print(hexagon2)
print(hexagon1 == hexagon2)
hexagon3 = Hexagon(5)
print(hexagon1 == hexagon3)
print(hexagon1 == hexagon2)