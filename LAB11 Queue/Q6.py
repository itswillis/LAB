class CircularQueue: 
    def __init__(self, capacity=8):
        self.items= [None]*capacity
        self.capacity = capacity
        self.count = 0 
        self.front =0
        self.back = capacity - 1

    def is_empty(self):
        if self.count == 0:
            return True
        return False
    
    def is_full(self):
        if self.count == self.capacity:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.back = (self.back + 1) % self.capacity
        self.items[self.back] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item
    
    def increase_capacity(self):
        self.capacity = self.capacity * 2
        temp_list = [None] * self.capacity
        if self.is_empty():
            self.back = self.capacity - 1
        else:
            i = 0
            num = self.front
            while i < self.count:
                temp_list[i] = self.items[num]
                num = int((num + 1) % (self.capacity / 2))
                i += 1
            self.back = self.count - 1
            self.front = 0
        self.items = temp_list
    
    def __str__(self):
        items = [None if i is None else i for i in self.items]
        return f"{items}, front:{self.front}, back:{self.back}, count:{self.count}"

try:
    q1 = CircularQueue(4)
    print(q1)
    q1.increase_capacity()
    print(q1)
except IndexError as err:
    print(err)