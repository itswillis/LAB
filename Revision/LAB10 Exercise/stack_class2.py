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

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.size())
my_stack.clear()
print(my_stack.size())
