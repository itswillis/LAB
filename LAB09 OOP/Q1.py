class Rectangle: 
    def __init__(self, width = 1, length = 1):
        self.width = width
        self.length = length 
    def get_area(self):
        return (self.width * self.length)
    def __str__(self):
        return ('Rectangle: {} x {}'.format(self.width, self.length))
    
r1 = Rectangle(3, 4)
print(r1)
print(r1.get_area())
r2 = Rectangle()
print(r2)
print(type(r1))