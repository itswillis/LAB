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
        if not self.items:
            raise IndexError ("ERROR: The queue is empty!")
        return self.items.pop()
        
    def peek(self):
        if not self.items:
            raise IndexError ("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def __str__(self):
        arrow = '->'
        end = '|'
        result = ', '.join(str(item) for item in self.items)
        final = arrow + ' ' + end + result + end + ' ' + arrow
        return final
        
try:
    q = Queue()
    q.enqueue(2)
    q.enqueue(1)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
except IndexError as err:
    print(err)
	
try:
    q = Queue()
    q.enqueue('a')
    print(q)
    q.dequeue()
    print(q)
    q.enqueue('b')
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
except IndexError as err:
    print(err)
