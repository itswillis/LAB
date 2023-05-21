class Region: 

    def __init__(self, name = "Unknown", land_area = 1):
        self.name = name
        self.land_area = land_area
        self.births_list = [] 
        self.deaths_list = []
    
    def __eq__(self, other): 
        if isinstance(other, Region):
            return self.name == other.name
        return False
    
    def __lt__(self, other):
        return self.name < other.name
    
    def add_birth_record(self, birth_record): 
        self.births_list.append(birth_record)

    def add_death_record(self, death_record): 
        self.deaths_list.append(death_record)
        
    def get_number_of_births(self, start_year, end_year):
        total_births = 0
        for i in self.births_list:
            if i.year >= start_year and i.year <= end_year:
                total_births += i.number_of_births
        return total_births

    def get_number_of_deaths(self, start_year, end_year):
        total_deaths = 0
        for i in self.deaths_list:
            if i.year >= start_year and i.year <= end_year:
                total_deaths += i.number_of_deaths
        return total_deaths
    
    def __str__(self): 
        return "{} ({} km^2)".format(self.name, self.land_area)
    
class Country: 

    def __init__(self, country_name = "Unknown", abbreviation = "N/A"):
        self.country_name = country_name
        self.abbreviation = abbreviation 
        self.regions_list = [] 

    def add_region(self, region): 
        self.regions_list.append(region)
        self.regions_list = sorted(self.regions_list)

    def __str__(self):
        if not self.regions_list:
            return "{} ({})\n".format(self.country_name, self.abbreviation)
        
        regions_info = "\n".join(str(region) for region in self.regions_list)
        return "{} ({})\n{}".format(self.country_name, self.abbreviation, regions_info)



            

sg = Country("Singapore", "SG")
print(sg)
nz = Country("New Zealand", "NZ")      
region1 = Region("Gisborne", 8385) 
region2 = Region("Bay of Plenty", 12072)
nz.add_region(region1)
nz.add_region(region2)
print(nz)