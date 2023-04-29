from math import sqrt
class EquilateralTriangle:
    def __init__(self, side_length = 1):
        self.side_length = side_length
    def get_area(self):
        return (sqrt(3) * self.side_length * (self.side_length/4))
    def __str__(self):
        return ('EquilateralTriangle({:.2f})'.format(self.get_area()))

triangle1  = EquilateralTriangle()
print(triangle1)
triangle2  = EquilateralTriangle(1)
print(triangle2)
triangle3 = EquilateralTriangle(5)
print(triangle3)
print(type(triangle1))
