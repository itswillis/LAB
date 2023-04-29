class Country:
    def __init__(self, country_name = "Unknown", abbreviation = "N/A", regions = []):
        self.country_name = country_name
        self.abbreviation = abbreviation
        self.regions = regions
    def get_country_name(self):
        return self.country_name
    def get_abbreviation(self):
        return self.abbreviation
    def get_regions(self):
        return self.regions
    
nz = Country("New Zealand", "NZ")
print(nz.get_country_name(), nz.get_abbreviation())
print(type(nz))
print(len(nz.get_regions()))
unknown = Country()
print(nz.get_country_name(), nz.get_abbreviation())
