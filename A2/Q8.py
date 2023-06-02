class Primes:

    def __init__(self, number_of_primes=5):
        self.number_of_primes = number_of_primes

    def __iter__(self):
        return PrimesIterator(self.number_of_primes)
    
class PrimesIterator:

    def __init__(self, number_of_primes=5):
        self.number_of_primes = number_of_primes
        self.count = 1
        self.current = 2
    
    def __next__(self):
        if self.count > self.number_of_primes:
            raise StopIteration
        else:
            while True:
                is_prime = True 
                for i in range(2, int(self.current/2)+1):
                    if (self.current % i) == 0:
                        is_prime = False
                        self.current += 1
                        break
                        
                if is_prime: 
                    self.current += 1
                    self.count += 1
                    return self.current - 1

sequence = Primes(10)
for prime in sequence:
    print(prime, end=" ")
print()