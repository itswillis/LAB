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

def create_numbers_stack(numbers):
    a_stack = Stack()
    for num in numbers:
        a_stack.push(num)
    return a_stack

def split_stack(a_stack):
    # create an odd stack
    odd_stack = Stack()
    # create an even stack
    even_stack = Stack()

    stack_list = []
    odd_list = []
    even_list = []

    # pop all these elements out of stack
    for _ in range(a_stack.size()):
        stack_list.append(a_stack.pop())

    # add them to odd and even str groups:
    for num in stack_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    # push items back on to the even and odd stacks

    # work with even stack first
    for num in even_list:
        even_stack.push(num)
    for num in odd_list:
        odd_stack.push(num)

    return (even_stack, odd_stack)

a_stack = create_numbers_stack([5, 7, 18, -2, 9, 4])
a_tuple = split_stack(a_stack)
print(type(a_tuple[0]), type(a_tuple[1]))
print(a_tuple[0])
print(a_tuple[1])
