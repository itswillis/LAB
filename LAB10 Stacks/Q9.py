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
    

def reverse_number(number):
    stack = Stack()

    for digit in str(number):
        stack.push(int(digit))

    reversed_number = 0
    while not stack.is_empty():
            reversed_number = reversed_number * 10 + stack.pop()
    return reversed_number

data = reverse_number(1234)
print(data)
print(type(data))

print(reverse_number(12))
print(reverse_number(1))
print(reverse_number(2364))