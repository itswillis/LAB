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
            

	
s1 = Stack()
for i in range(4,7):
    s1.push(i)
s2 = Stack()
for i in range(4,7):
    s2.push(i)
s3 = Stack()
for i in range(6,3,-1):
    s3.push(i)
s4 = s1
print("s1==s2:", s1 == s2)
print("s1==s3:",s1 == s3)
print("s1==s4:",s1 == s4)
print("s1 is s2:",s1 is s2)
print("s1 is s4:",s1 is s4)
print("s1", s1)
print("s2", s2)
print("s3", s3)
print("s4", s4)
