class SimpleHashTable:

    def __init__(self, size = 7):
        self.size = size
        self.slots = size * [None]

    def __str__(self):
        return str(self.slots)
    
    def get_hash_index(self, key):
        modulus = key % self.size
        return modulus
    
    def put(self, key):
        if self.is_full():
            raise IndexError("ERROR: The hash table is full.")
        
        self.probe_count = 1
        self.modulus = key % self.size

        while self.slots[self.modulus] is not None:
            self.probe_count += 1
            self.modulus = (self.modulus + 1) % self.size
    
        self.slots[self.modulus] = key
    
    def is_empty(self):
        for slot in self.slots:
         if slot is not None:
            return False
        return True
    
    def is_full(self):
        for slot in self.slots:
         if slot is None:
            return False
        return True
    
    def clear(self):
        self.slots = self.size * [None]

    def __len__(self):
        return sum(self.slots)

try:
    my_hash_table = SimpleHashTable(3)
    my_hash_table.put(13) 
    my_hash_table.put(26) 
    my_hash_table.put(39)
    my_hash_table.put(52)
except IndexError as e:
    print(e)
print(my_hash_table)
print(my_hash_table.is_empty())
my_hash_table.clear()
print(my_hash_table.is_empty())