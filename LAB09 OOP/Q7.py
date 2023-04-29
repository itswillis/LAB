class Country:
    def __init__(self, name="Unknown", abbreviation=""):
        self.name = name
        self.abbreviation = abbreviation

    def get_name(self):
        return self.name

    def get_abbreviation(self):
        return self.abbreviation

    def __str__(self):
        return "{} ({})".format(self.name, self.abbreviation)

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

    
nz_country = Country("New Zealand", "NZ")
region1 = Region("Auckland", 1695200, 4941, nz_country)
print(region1)