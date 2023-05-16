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
    
    def add_after(self, value):
        new_node = Node(value)
        new_node.set_next(self.get_next())
        self.set_next(new_node)

    def multi_add(self, a_list):
        # takes a python list (a_list) of values and adds Nodes for all elements from the a_list, to after the current Node object.
        current = self 
        for value in a_list: 
            new_node = Node(value)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            current = new_node
    
    def remove_after(self):
        if self.next:
            self.next = self.next.get_next()

def get_list(a_node):
    result = []
    current_node = a_node
    while current_node is not None:
        result.append(current_node.data)
        current_node = current_node.get_next()
    return result

def print_node_chain(a_node):
    if a_node is None:
        print()
        return
    print (a_node.get_data(), end=' ')
    
    print_node_chain(a_node.get_next())

def join_chains(node1, node2):
    current_node = node1
    # Traverse to the end of the chain
    while current_node.get_next() is not None:
        current_node = current_node.get_next()

    current_node.set_next(node2)

def reverse_node_chain(a_node):
    new_chain = Node(a_node.get_data())

    current_node = a_node.get_next()
    
    while current_node is not None:
        new_node = Node(current_node.get_data())
        
        new_node.set_next(new_chain)
        new_chain = new_node

        current_node = current_node.get_next()
    
    return new_chain


node1 = Node('hello')
node2 = Node('world')
node1.set_next(node2)
result = reverse_node_chain(node1)
print_node_chain(result)
print_node_chain(node1)
if not isinstance(result, Node):
    print("result must be an object of the Node class")