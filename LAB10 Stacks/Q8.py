class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def __str__(self):
        stack_str = str(self.items)
        return stack_str[:-1] + " <-"

    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self.items == other.items
    
s1 = Stack()
for i in range(4,7):
    s1.push(i)
list1 = [4, 5, 6]
print("s1", s1)
print("list1", list1)
print(s1 == list1)