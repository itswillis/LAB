class Region: 
    def __init__(self, name = "Unknown", population = 1, land_area = 1):
        self.name = name
        self.population = population
        self.land_area = land_area

    def get_name(self):
        return self.name 

    def  get_population(self):
        return self.population

    def get_land_area(self):
        return self.land_area


region1 = Region("Bay of Plenty", 347700, 12072)
region2 = Region("Gisborne", 52100, 8385)
region3 = Region()
print(region1.get_name())
print(region2.get_name())
print(region3.get_name())
print(region1.get_name(), region1.get_population(), region1.get_land_area())
print(type(region1))
print(region1 == region2)