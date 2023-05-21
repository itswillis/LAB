class Region: 
    def __init__(self, name = "Unknown", land_area = 1):
        self.name = name
        self.land_area = land_area

    def __str__(self): 
        return "{} ({} km^2)".format(self.name, self.land_area)
    
    def __eq__(self, other): 
        if isinstance(other, Region):
            return self.name == other.name
        return False
    
    def __lt__(self, other):
        return self.name < other.name


region1 = Region("Bay of Plenty", 12072)
region2 = Region("Gisborne", 8385)
region3 = Region()
print(region1)
print(region2)
print(region3)
print(region1 == region2)
print(region2 == region3)
print(region1 < region2)
print(region2 < region3)
print(region1 == 'Gisborne')