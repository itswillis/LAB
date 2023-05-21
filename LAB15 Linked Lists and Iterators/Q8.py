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

class LinkedList:
    def __init__(self, head = None, length = 0):
        self.head = head
        self.length = length
    
    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def __len__(self):
        return self.length
    
    def get_head(self):
        return self.head
    
    def clear(self):
        self.head == None
        self.length = 0 

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def __str__(self):
        if self.is_empty():
            return ""
        else:
            result = "Head: "
            current = self.head
            while current != None:
                result = result + str(current.data) + " --> "
                current = current.next # update current or else infinite loop
            return result[:-5] # remove extra arrows at the end
        
    def remove_from_head(self):
            if self.is_empty():
                return None
            else:
                current = self.head
                self.head = current.get_next()
                self.length -= 1
                return current
            
    def remove_from_tail(self):
        if self.is_empty():
            return None
        
        current = self.head
        previous = None

        # continue until the current node is the last one
        while current.next != None:
            previous = current # update previous to be the current node
            current = current.next # move to the next node

        # current is the last node in the linked list
        if previous is None:
            self.head = None
        else:
            previous.next = None 
        self.length -= 1
        return current
    
    def search(self, search_value):
        current = self.head
        while current != None:
            if current.get_data() == search_value:
                return True
            else:
                current = current.get_next()
        return False
    
    def __iter__(self):
        return LinkedListIterator(self.head)
    
class LinkedListIterator: 

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

values = LinkedList()
values.add('cherry')
values.add('banana')
values.add('apple')
for value in values:
    print(value)