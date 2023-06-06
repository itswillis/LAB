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

    
def evaluate_postfix(postfix):
    stack = Stack()

    for token in postfix:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '/':
                result = operand1 // operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '%':
                result = operand1 % operand2
            stack.push(result)

                
    return stack.pop()
                

print(evaluate_postfix('243*%'))
print(evaluate_postfix('942-5*%3-'))

        
