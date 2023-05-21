class Tribonacci:

    def __init__(self, term1=0, term2=0, term3=1, num_terms=5):
        self.term1 = term1
        self.term2 = term2
        self.term3 = term3
        self.num_terms = num_terms

    def __iter__(self):
        return TribonacciIterator(self.term1, self.term2, self.term3, self.num_terms)
    
class TribonacciIterator: 
    
    def __init__(self, term1 = 0, term2 = 0, term3 = 1, num_terms = 5):
        self.term1 = term1
        self.term2 = term2
        self.term3 = term3
        self.num_terms = num_terms
        self.current_count = 0

    def __next__(self):
        if self.current_count >= self.num_terms:
            raise StopIteration

        if self.current_count == 0:
            result = self.term1
        elif self.current_count == 1:
            result = self.term2
        elif self.current_count == 2:
            result = self.term3
        else:
            next_term = self.term1 + self.term2 + self.term3
            self.term1 = self.term2
            self.term2 = self.term3
            self.term3 = next_term
            result = next_term

        self.current_count += 1
        return result
        
sequence = Tribonacci()
for number in sequence:
    print(number, end=" ")
print()