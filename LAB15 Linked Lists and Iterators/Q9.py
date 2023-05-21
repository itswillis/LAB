class OddNumber:

    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def __iter__(self):
        return OddNumberIterator(self.upper_limit)

class OddNumberIterator:

    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.current = 1

    def __next__(self):
        if self.current > self.upper_limit:
            raise StopIteration
        else:
            current_number = self.current
            self.current += 2
            return current_number


values = OddNumber(5)
for x in values:
    print(x)