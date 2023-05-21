class Births: 
    def __init__(self, year = 1990, number_of_births = 0):
        self.year = year
        self.number_of_births = number_of_births

    def __str__(self):
        return "Births: {} ({})".format(self.number_of_births, self.year)
    
class Deaths: 
    def __init__(self, year = 1990, number_of_deaths = 0):
        self.year = year
        self.number_of_deaths = number_of_deaths

    def __str__(self):
        return "Deaths: {} ({})".format(self.number_of_deaths, self.year)

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

    def search_region(self, region_name):
        for region in self.regions_list: 
            if region.name == region_name:
                return region 
        return None 
    
    # We need to get the number of births from the Region class
    def print_births_table(self, start_year, end_year): 
        for region in self.regions_list: 
            births = region.get_number_of_births(start_year, end_year)
            print("{:<18}|{}".format(region.name, births))

    def print_deaths_table(self, start_year, end_year):
        for region in self.regions_list:
            deaths = region.get_number_of_deaths(start_year, end_year)
            print("{:<18}|{}".format(region.name, deaths))

    def get_total_births(self, start_year, end_year):
        total_births = 0 
        for region in self.regions_list: # To calculate the total number of births and deaths for all regions within the start and end years
            total_births += region.get_number_of_births(start_year, end_year)
        return total_births
    
    def get_total_deaths(self, start_year, end_year):
        total_deaths = 0
        for region in self.regions_list: # To calculate the total number of deaths and deaths for all regions within the start and end years
            total_deaths += region.get_number_of_deaths(start_year, end_year)
        return total_deaths

    def __str__(self):
        if not self.regions_list:
            return "{} ({})\n".format(self.country_name, self.abbreviation)
        
        regions_info = "\n".join(str(region) for region in sorted(self.regions_list))
        return "{} ({})\n{}".format(self.country_name, self.abbreviation, regions_info)
    
# Helper function - Display Banner
def display_banner(): 
    print("*" * 35)
    print("Welcome to Births/Deaths Statistics")
    print("*" * 35)

# Helper function - 
def get_country_info(): 
    name_of_country = input("Enter the name of a country: ")
    abbreviation_of_country = input("Enter the abbreviation of a country: ")
    return name_of_country, abbreviation_of_country

#Helper function - Reading regions file
def read_regions_file(filename, country):
    try:
        with open(filename, "r") as f: 
            for line in f: 
                region_data = line.strip().split("\t")
                try:
                    land_area = int(region_data[1])
                    if land_area <= 0:
                        raise ValueError("Land area must be greater than 0.")
                except ValueError:
                    # Skip the record if land area is not a valid integer
                    continue
                region = Region(name=region_data[0], land_area=land_area)
                country.regions_list.append(region)
    except FileNotFoundError:
        print("ERROR: The file '{}' does not exist.".format(filename))


# Helper function - Reading birth/stats statistics
def read_stats_file(filename, country):
    with open(filename, "r") as f:
        for line in f:
            stats_data = line.strip().split("\t")
            year = int(stats_data[0])
            event_type = stats_data[1]
            region_name = stats_data[2]
            count = int(stats_data[3])

            if event_type == "Births":
                record = Births(year=year, number_of_births=count)
            elif event_type == "Deaths":
                record = Deaths(year=year, number_of_deaths=count)

            region = country.search_region(region_name)
            if region:
                if event_type == "Births":
                    region.add_birth_record(record)
                elif event_type == "Deaths":
                    region.add_death_record(record)
    
def main():
    display_banner()
    name_of_country, abbreviation_of_country = get_country_info()
    country = Country(country_name=name_of_country, abbreviation=abbreviation_of_country)

    
    filename = input("Enter the filename for reading a list of regions: ")
    read_regions_file(filename, country)

    filename = input("Enter the filename for reading Births/Deaths data: ")
    read_stats_file(filename, country)

    start_year = 2018
    end_year = 2022
    total_births = country.get_total_births(start_year, end_year)
    total_deaths = country.get_total_deaths(start_year, end_year)

    print("Total births between {} and {}: {}".format(start_year, end_year, total_births))
    print("Total deaths between {} and {}: {}".format(start_year, end_year, total_deaths))