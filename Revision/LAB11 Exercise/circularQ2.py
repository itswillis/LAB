class CircularQueue:

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.front = 0
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def __str__(self):
        result = (f'{self.items}, front:{self.front}, back:{self.back}, count:{self.count}')
        return (result)

    def is_full(self):
        if self.count == self.capacity:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        else:
            self.back = (self.back + 1) % self.capacity
            self.items[self.back] = item
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        else:
            item = self.items[self.front]
            self.front = (self.front +1)% self.capacity
            self.count -= 1
            return item

q1 = CircularQueue(4)
print(q1)
q1.enqueue(1)
print(q1)
q1.enqueue(2)
print(q1)
q1.enqueue(3)
print(q1)
q1.enqueue(4)
print(q1)
print("Full?", q1.is_full())
print("Empty?", q1.is_empty())
