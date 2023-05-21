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

def create_a_test_tree():
    tree = BinaryTree(41)
    tree.insert_left(20)
    tree.insert_right(65)
    left = tree.get_left()
    left.insert_left(11)
    left.insert_right(29)
    leftright = left.get_right()
    leftright.insert_right(32)
    right = tree.get_right()
    right.insert_left(50)
    right.insert_right(91)
    rightright = right.get_right()
    rightright.insert_left(72)
    rightright.insert_right(99)
    return tree

    '''
        41
       /  \
     20    65
    / \   /  \
  11  29 50  91
      \     /  \
      32   72  99
      
    '''

tree1 = create_a_test_tree()    
print(get_sum_leaf_nodes(tree1))
