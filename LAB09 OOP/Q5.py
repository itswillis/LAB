from math import sqrt

class EquilateralTriangle:
    def __init__(self, side_length=1):
        self.side_length = side_length
        
    def get_area(self):
        return sqrt(3) * self.side_length**2 / 4
        
    def __str__(self):
        return 'EquilateralTriangle({:.2f})'.format(self.get_area())

class Container: 
    def __init__(self, name="Unknown", triangles=None):
        self.name = name
        self.triangles = triangles or []
        
    def get_name(self):
        return self.name
    
    def get_triangles(self):
        return self.triangles
    
    def add_triangle(self, triangle):
        self.triangles.append(triangle)
        
    def __str__(self):
        if not self.triangles:
            return 'Name: {}\nNo triangles.'.format(self.name)
        else:
            triangles_str = '\n'.join(str(triangle) for triangle in self.triangles)
            return 'Name: {}\nTriangle(s):\n{}'.format(self.name, triangles_str)

container1 = Container("ONE")
container1.add_triangle(EquilateralTriangle(2))
container1.add_triangle(EquilateralTriangle(4)) 
print(container1)
print()
container2 = Container("TWO")
print(container2)
