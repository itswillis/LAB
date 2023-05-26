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
    
    def insert(self, value):
        # if value already in BST return 
        if value == self.data:
            return
        # else find a place to store
        elif value < self.data:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1)

def create_bst_from_list(values):
    tree = BinarySearchTree(values[0])
    for value in values:
        tree.insert(value)
    return tree

def find_node(bst, value):
    if bst is None:
        return None
    
    if bst.data == value:
        return bst # does not return the original bst, returns the node with value. 
    
    elif value < bst.data: 
        return find_node(bst.left, value)
    
    elif value > bst.data:
        return find_node(bst.right, value)
    
def sum_tree(node):
    if node is None:
        return 0 
    else:
        # calculate the sum of all values in the tree, include the node and leaves
        return sum_tree(node.left) + node.data + sum_tree(node.right)

def get_difference_beneath(bst, value):
    node = find_node(bst, value)
    if node is None:
        return 0
    else: 
        left_sum = sum_tree(node.left)
        right_sum = sum_tree(node.right)
        difference = left_sum - right_sum
        return difference

tree2 = BinarySearchTree(7, BinarySearchTree(2, BinarySearchTree(1), BinarySearchTree(5)), BinarySearchTree(9),)
print('Sum beneath 5 =', get_difference_beneath(tree2, 7))