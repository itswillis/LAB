# define a constructor 
class Hexagon:
    def __init__(self, side_length = 1):
         self.side_length = side_length

    def set_side_length(self, side_length):
        if side_length > 0: 
            self.side_length = side_length

    def get_side_length(self):
        return self.side_length

    
hexagon1 = Hexagon()
print(hexagon1.get_side_length())
hexagon2 = Hexagon(12)
print(hexagon2.get_side_length())
hexagon1.set_side_length(-1)
print(hexagon1.get_side_length())
hexagon1.set_side_length(12)
print(hexagon1.get_side_length())
hexagon3 = Hexagon(1)
print(hexagon1 == hexagon3)