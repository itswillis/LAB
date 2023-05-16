class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
    
    def __str__(self):
        return (f"{self.data}")

node2 = Node('world')
node1 = Node('hello', node2)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1)
print(node2)