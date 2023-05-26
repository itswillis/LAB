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
        self.probe_count = 1
        self.modulus = key % self.size

        while self.slots[self.modulus] is not None:
            self.probe_count += 1
            self.modulus = (self.modulus + 1) % self.size
    
        self.slots[self.modulus] = key

my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(14)
my_hash_table.put(15)
my_hash_table.put(16)
my_hash_table.put(17)
print(my_hash_table)