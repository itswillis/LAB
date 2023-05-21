class GeometricSequence:
    def __init__(self, first_term=1, common_ratio=2, n=5):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.number_of_terms = n        
    def __iter__(self):
        return GeometricIterator(self.first_term, self.common_ratio, self.number_of_terms)
    
class GeometricIterator:
    def __init__(self, first_term = 1, common_ratio = 2, number_of_terms = 5):
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.current_count = 1
        self.number_of_terms = number_of_terms

    def __next__(self):
        # check if current count is greater than the number of terms
        if self.current_count > self.number_of_terms:
            raise StopIteration
        else: 
            result = self.first_term * (self.common_ratio ** (self.current_count - 1))
            self.current_count += 1
            return result

values = GeometricSequence(2, 10, 3)
for x in values:
    print(x)