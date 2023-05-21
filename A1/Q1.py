class Births: 
    def __init__(self, year = 1990, number_of_births = 0):
        self.year = year
        self.number_of_births = number_of_births

    def __str__(self):
        return "Births: {} ({})".format(self.number_of_births, self.year)

birth1 = Births(2018, 2181)
birth2 = Births(2019, 20712)
birth3 = Births()
print(birth1)
print(birth2)
print(birth3)