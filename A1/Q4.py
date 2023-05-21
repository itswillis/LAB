class Region: 
    def __init__(self, name = "Unknown", land_area = 1):
        self.name = name
        self.land_area = land_area
        self.births_list = [] 
        self.deaths_list = []

    def __str__(self): 
        return "{} ({} km^2)".format(self.name, self.land_area)
    
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

region1 = Region("Bay of Plenty", 12072)
birth1 = Births(2018, 3969)
birth2 = Births(2019, 4047)
death1 = Deaths(2018, 2583)
death2 = Deaths(2019 ,2787)
region1.add_birth_record(birth1)
region1.add_birth_record(birth2)
region1.add_death_record(death1)
region1.add_death_record(death1)
print(region1.get_number_of_births(2018, 2018))
print(region1.get_number_of_births(2018, 2019))
print(region1.get_number_of_births(2018, 2020))
print(region1.get_number_of_births(2020, 2020))
print(region1.get_number_of_deaths(2018, 2019))