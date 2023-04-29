class Region:
    def __init__(self, name="Unknown", population=1, land_area=1, country=None):
        self.name = name
        self.population = population
        self.land_area = land_area
        self.country = country

    def get_name(self):
        return self.name

    def get_population(self):
        return self.population

    def get_land_area(self):
        return self.land_area

    def get_density(self):
        return round(self.population / self.land_area, 2)

    def get_country(self):
        return self.country

    def __str__(self):
        if self.country is None:
            return "{}, density = {:.2f} people per sq. km.".format(self.name, self.get_density())
        else:
            return "{}({}), density = {:.2f} people per sq. km.".format(self.name, self.country.get_abbreviation(), self.get_density())

class Country:
    def __init__(self, country_name = "Unknown", abbreviation = "N/A", regions = None):
        self.country_name = country_name
        self.abbreviation = abbreviation
        self.regions = regions if regions is not None else []

    def get_country_name(self):
        return self.country_name
    
    def get_abbreviation(self):
        return self.abbreviation
    
    def get_regions(self):
        return self.regions
        
    def add_region(self, region):
        self.regions.append(region)

    def __str__(self):
        if not self.regions:
            return '{}({})\n'.format(self.country_name, self.abbreviation)
        else:
            regions_str = '\n'.join(str(region) for region in self.regions)
            return '{}({})\n{}'.format(self.country_name, self.abbreviation, regions_str)
        
    def get_total_population(self):
        return sum(region.get_population() for region in self.regions)

sg = Country("Singapore", "SG")
print(sg.get_total_population())
nz = Country("New Zealand", "NZ")
region1 = Region("Bay of Plenty", 347700, 12072, nz)
region2 = Region("Gisborne", 52100, 8385, nz)
nz.add_region(region1)
nz.add_region(region2)
print(nz.get_total_population())
