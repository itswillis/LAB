class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    
    def list_enqueue(self, item_list):
        for item in item_list:
            self.enqueue(item)
        return item_list
    
    def list_dequeue(self, number):
        if number > self.size():
            raise IndexError("ERROR: There are not enough items in the queue!")
        
        dequeued_items = [] 
        for _ in range(number):
            item = self.dequeue()
            dequeued_items.append(item)

        return dequeued_items
    
    def reverse(self):
        self.items.reverse()

    def combine(self, other_queue):
        for item in reversed(other_queue.items):
            self.enqueue(item)

    def __str__(self):
        return "-> |{}| ->".format(", ".join(str(item) for item in self.items))
    
q1 = Queue()
q2 = Queue()
q1.list_enqueue([1, 2, 3, 4])
q2.list_enqueue(["A", "B", "C"])
print("Queue 1:", q1)
print("Queue 2:", q2)
q1.combine(q2)
print("Queue 1:", q1)
print("Queue 2:", q2)