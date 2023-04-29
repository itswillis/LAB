class Container: 
    def __init__(self, name = "Unknown", triangles = []):
        self.name = name
        self.triangles = triangles
    def get_name(self):
        return (self.name)
    def get_triangles(self):
        return (self.triangles)

container1 = Container()
print(container1.get_name())
print(container1.get_triangles())
container2 = Container("First")
print(container2.get_name())
print(container2.get_triangles())