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
    
hexagon1 = Hexagon()
print(hexagon1.get_perimeter(), hexagon1.get_area())
hexagon2 = Hexagon(2)
print(hexagon2.get_perimeter(), hexagon2.get_area())

hexagon = Hexagon(4)
print(hexagon.get_side_length())
print(hexagon.get_perimeter(), hexagon.get_area())
hexagon2 = Hexagon(4)
print(hexagon == hexagon2)
print(type(hexagon))