class Node: 
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next

class OrderedList:
    def __init__(self, head = None, length = 0):
        self.head = head
        self.length = length 

    def __len__(self):
        current = self.head
        total = 0 
        while current != None:
            total += 1 
            current = current.next
        return total
    
    def is_empty(self):
        return self.head is None
    
    def add(self, value):
        new_node = Node(value)
        current = self.head
        previous = None
        
        while current is not None and current.get_data() < value:
            previous = current
            current = current.get_next()
            
        new_node.set_next(current)
        
        if previous is None:
            self.head = new_node
        else:
            previous.set_next(new_node)

    def search(self, value):
        current = self.head
        while current != None:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False
    
    def remove(self, value):
        # lets try find the data first
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
                return current.data
            else:
                previous.set_next(current.get_next())
                return current.data
    
    def __str__(self):
        if self.is_empty():
            return ""
        else:
            result = "Head:"
            current = self.head
            while current != None:
                result = result + ' ' + str(current.data) + ' ' + '-->'
                current = current.next
            return result[:-4]
        
	
	
o_list = OrderedList()
print("Is the ordered list empty?", o_list.is_empty())
for i in range(5, -1, -1):
    o_list.add(i)
print("Ordered List:", o_list)
value = 6
print(f"Is {value} in the ordered list? {o_list.search(value)}")
value = -1
print(f"Is {value} in the ordered list? {o_list.search(value)}")