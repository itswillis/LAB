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

    def reverse(self):

        a =[]
        length = self.size()
        
        for items in self.items:
            a.append(items)

        # dequeue all 5 items
        for item in range(length):
            self.dequeue()

        # enqueue agai, this will be in reversed order
        for item in (a):
            self.enqueue(item)

    def combine(self, other_queue):
        # pop all of the elements and append them to a list
        a_list = []
        for i in range(other_queue.size()):
            a = other_queue.dequeue()
            a_list.append(a)

        # add the elements in the list to the self queue
        for items in a_list:
            self.enqueue(items)
            other_queue.enqueue(items) # add the elements back into the other queue
    
q1 = Queue()
q2 = Queue()
q1.list_enqueue([1, 2, 3, 4])
q2.list_enqueue(["A", "B", "C"])
print("Queue 1:", q1)
print("Queue 2:", q2)
q1.combine(q2)
print("Queue 1:", q1)
print("Queue 2:", q2)
