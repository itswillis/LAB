class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)[:-1] + ' <-'	

def editor_do_undo(stack, commands):
    # keep track of characters we have undone
    undos = Stack()
    for command in commands:
        if command == "CTRL+Z" and not stack.is_empty():
            undos.push(stack.pop())
        elif command == "CTRL+Y" and not undos.is_empty():
            stack.push(undos.pop())
    result = ""
    while not stack.is_empty():
        result = stack.pop() + result
    return result

my_string = "hello world"
my_stack = Stack()
for char in my_string:
    my_stack.push(char)
print(my_stack)
changes = ["CTRL+Z", "CTRL+Z", "CTRL+Y"]
print(f"String after editing: {editor_do_undo(my_stack, changes)}")


