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
    
def convert_tree_to_list(tree):
    if tree == None:
        return None
    else: 
        result = []
        result.append((tree.get_data()))
        result.append(convert_tree_to_list(tree.get_left()))  
        result.append(convert_tree_to_list(tree.get_right()))
        return result
    
def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data()))
    if t.get_left() != None:
        print('(L)', end ='')
        print_tree(t.get_left(), level + 1)
    if t.get_right() != None: 
        print('(R)', end ='')
        print_tree(t.get_right(), level + 1)

def create_tree_from_nested_list(a_list):
    # Base case: if the list is None, return None
    if a_list is None:
        return None
    
    # The first item in the list is the root
    root = BinaryTree(a_list[0])

    # If there's a second item in the list (the left subtree), 
    # recursively call this function on that item to create the left child
    if len(a_list) > 1:
        root.left = create_tree_from_nested_list(a_list[1])

    # If there's a third item in the list (the right subtree), 
    # recursively call this function on that item to create the right child
    if len(a_list) > 2:
        root.right = create_tree_from_nested_list(a_list[2])

    return root

    
tree = create_tree_from_nested_list([10, [5, None, None], [15, [11, None, None], [22, None, None]]])
print_tree(tree, 0)