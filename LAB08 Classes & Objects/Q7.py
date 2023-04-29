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
    
    def get_density(self):
        population_density = self.population / self.land_area
        return round(population_density, 2)
    
    def __str__(self):
        return ("{}, density = {:.2f} people per sq. km.".format(self.name, self.get_density()))

region1 = Region("Bay of Plenty", 347700, 12072)
region2 = Region("Gisborne", 52100, 8385)
region3 = Region()
print(region1.get_density())
print(region2.get_density())
print(region3.get_density())
print(region1)
print(region2)
print(region3)