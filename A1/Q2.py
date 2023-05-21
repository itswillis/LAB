class Deaths: 
    def __init__(self, year = 1990, number_of_deaths = 0):
        self.year = year
        self.number_of_deaths = number_of_deaths

    def __str__(self):
        return "Deaths: {} ({})".format(self.number_of_deaths, self.year)


death1 = Deaths(2018, 2181)
death2 = Deaths(2019, 20712)
death3 = Deaths()
print(death1)
print(death2)
print(death3)