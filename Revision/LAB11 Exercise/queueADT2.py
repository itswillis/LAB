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

    def list_enqueue(self, item_list):
        for item in item_list:
            self.enqueue(item)

    def list_dequeue(self, number):

        if number > self.size():
            raise IndexError ("ERROR: There are not enough items in the queue!")

        dequeued_list = []
        for _ in range(number):
            item = self.dequeue()
            dequeued_list.append(item)

        return dequeued_list
	
q = Queue()
q.list_enqueue([1, 2, 3, 4])
q.enqueue("A")
print("Queue:", q)

try:
    q = Queue()
    q.list_enqueue([1, 2, 3, 4, 5])
    print("Queue:", q)
    print("Dequeued items:", q.list_dequeue(3))
    print("Queue:", q)
except IndexError as err:
    print(err)


try:
    q = Queue()
    q.list_enqueue([1, 2, 3, 4, 5])
    print("Dequeued items:", q.list_dequeue(6))
    print("Queue:", q)
except IndexError as err:
    print(err)
