class CircularQueue:

    def __init__(self, capacity = 8):
        self.front = 0
        self.capacity = capacity
        self.back = self.capacity - 1
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def __str__(self):
        a_list = [None] * self.capacity
        result = (f'{a_list}, front:{self.front}, back:{self.back}, count:{self.count}')
        return (result)

q1 = CircularQueue()
print(q1)
print(q1.is_empty())
print(type(q1))


q1 = CircularQueue(5)
print(q1)
