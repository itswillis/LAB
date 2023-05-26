class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t
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

def create_a_bigger_tree():
    tree = BinaryTree('a')
    tree.insert_left('b')
    tree.insert_right('c')
    left = tree.get_left()
    left.insert_left('d')
    left.insert_right('e')
    leftleft = left.get_left()
    leftright = left.get_right()
    leftleft.insert_right('f')
    leftright.insert_right('g')
    return tree

def get_height(tree): 
    if tree == None: 
        return -1
    else:
        return 1 + max(get_height(tree.get_left()), \
                       get_height(tree.get_right()))

def get_sum_leaf_nodes(my_tree):
    # this should return the sum of leaf nodes, not include the nodes in the subtree
    if my_tree == None: 
        return 0 
    # recursive approach
    elif (my_tree.get_left() == None and my_tree.get_right() == None):
        return my_tree.get_data()
    else: 
        return get_sum_leaf_nodes(my_tree.get_left()) + get_sum_leaf_nodes(my_tree.get_right()) 

def print_inorder(tree):
    # in order => LEFT, ROOT, RIGHT
    if tree != None:
        print_inorder(tree.get_left()) # LEFT
        print(tree.get_data(), end= ' ') # ROOT 
        print_inorder(tree.get_right()) # RIGHT

from queue import Queue
def print_level_order(tree):
    if tree is None:
        return
    
    q = Queue()

    q.put(tree)

    while not q.empty():
        node = q.get()

        print(node.get_data(), end= " ")

        if node.get_left() is not None:
            q.put(node.get_left())
        
        if node.get_right() is not None:
            q.put(node.get_right())

def create_a_test_tree():
    tree = BinaryTree(10)
    tree.insert_left(5)
    tree.insert_right(19)
    left = tree.get_left()
    right = tree.get_right()
    left.insert_left(1)
    left.insert_right(6)
    right.insert_left(17)
    right.insert_right(21)
    return tree

    '''
        10
       /  \
     5     19       # IN ORDER => 1, 5, 6, 10, 17, 19, 21
    / \   /  \
  1    6 17  21

  '''

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
    
def is_binary_search_tree(my_tree, min_value, max_value):
    # check if the node is none, return True if it is: 
    if my_tree is None:
        return True
    # return FALSE if the value of the node is smaller than min_value or greater than max_value
    if my_tree.data < min_value or my_tree.data > max_value:
        return False
    # return the result of testing if the value of the left child is smaller than the value of the node, 
    result_left = is_binary_search_tree(my_tree.left, min_value, my_tree.data)
    result_right = is_binary_search_tree(my_tree.right, my_tree.data, max_value)

    if result_left == False or result_right == False:
        return False
    else:
        return True
    
def create_bst_from_sorted_list(sorted_list):  
    # base case
    if not sorted_list:
        return None 
    
    mid = len(sorted_list) // 2

    root_value = sorted_list[mid]

    root = BinaryTree(root_value)

    root.left = create_bst_from_sorted_list(sorted_list[:mid])

    root.right = create_bst_from_sorted_list(sorted_list[mid+1:])

    return root

tree = create_bst_from_sorted_list([1, 3, 5, 7, 9, 11, 13])
print_tree(tree, 0)

