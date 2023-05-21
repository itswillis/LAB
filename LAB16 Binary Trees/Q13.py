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
    

tree1 = create_a_test_tree()    
print_inorder(tree1)