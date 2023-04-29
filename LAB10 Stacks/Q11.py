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

def create_numbers_stack(numbers):
    a_stack = Stack()
    for num in numbers:
        a_stack.push(num)
    return a_stack

def split_stack(a_stack):
    even_stack = Stack()
    odd_stack = Stack()
    
    while not a_stack.is_empty():
        num = a_stack.pop()
        if num % 2 == 0:
            even_stack.push(num)
        else:
            odd_stack.push(num)
    
    return (even_stack, odd_stack)

def evaluate_postfix(postfix):
    stack = Stack()

    for token in postfix:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 // operand2
            elif token == "%":
                result = operand1 % operand2
            stack.push(result)

    return stack.pop()

print(evaluate_postfix('29+'))