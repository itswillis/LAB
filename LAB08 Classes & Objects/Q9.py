class GeometricSequence: 
    # first_term = 1 -> default
    # common ratio = 2 -> default

    def __init__(self, first_term = 1, common_ratio = 2):
        self.first_term = first_term
        self.common_ratio = common_ratio

    def get_nth_term(self, n):
        an = self.first_term * (self.common_ratio)**(n-1)
        return round(an, 3)
    
    def sum_to_n(self, n):
        if self.common_ratio != 1:
            sum = self.first_term * ((1 - self.common_ratio**n)/(1 - self.common_ratio))
        else: 
            sum = n * self.first_term

        return round(sum, 3)

sequence1 = GeometricSequence(0.25, 0.5)
print(sequence1.get_nth_term(4))
print(sequence1.sum_to_n(4))
sequence2 = GeometricSequence()
print(sequence2.get_nth_term(5))
print(sequence2.sum_to_n(5))

sequence2 = GeometricSequence(-4, -0.5)
print(sequence2.get_nth_term(5))
print(sequence2.sum_to_n(5))