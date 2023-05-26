class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def get_left(self):
        return self.left
        
    def get_right(self):
        return self.right
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right
    
    def __contains__(self, value):
        # base case
        if value == self.data:
            return True
        elif value < self.data and self.left != None:
            return self.left.__contains__(value)
        elif value > self.data and self.right != None:
            return self.right.__contains__(value)
        else:
            return False

tree1 = BinarySearchTree(7, BinarySearchTree(2, BinarySearchTree(1), BinarySearchTree(5)), BinarySearchTree(9),)

print(9 in tree1)
print(29 in tree1)