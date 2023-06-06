class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()
    def peek(self):
        if not self.items:
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = [] # re-initialise empty stack
    def __str__(self):
        item = str(self.items)
        item = item[:-1] # get rid of the closing bracket
        arrow = ' <-'
        result = item + arrow
        return result
    def __eq__(self, other):
        if isinstance(other, Stack):
            return self.items == other.items
        return False

def reverse_number(number):
    a_stack = Stack()

    number = str(number)
    # add numbers to a_stack
    for num in number:
        a_stack.push(num)

    empty = ''

    while not a_stack.is_empty():
        # LIFO
        popped = a_stack.pop()
        empty += popped
    return int(empty)

data = reverse_number(1234)
print(data)
print(type(data))
