from queue_array import Queue

# TreeNode is a node in the BinarySearchTree
class TreeNode:
    # init the node
    # key is an int
    # data is an int
    # left is a TreeNode or None
    # right is a TreeNode or None
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
    
    # Helper function for tree_height which recursively counts the layers in the recursion tree
    # node is a TreeNode
    # returns an int
    def get_height(self, node):
        if node == None:
            return -1
        left_amount = self.get_height(node.left)
        right_amount = self.get_height(node.right)
        if left_amount > right_amount:
            return left_amount + 1
        return right_amount + 1
    
    # Helper function for inorder_list which recursively makes an inorder list
    # returns an list
    def get_inorder_list(self):
        inorder_list = []
        if self.left != None:
            inorder_list += self.left.get_inorder_list()
        inorder_list.append(self.key)
        if self.right != None:
            inorder_list += self.right.get_inorder_list()
        return inorder_list
    
    # Helper function for preorder_list which recursively makes an preorder list
    # returns an list
    def get_preorder_list(self):
        preorder_list = [self.key]
        if self.left != None:
            preorder_list += self.left.get_preorder_list()
        if self.right != None:
            preorder_list += self.right.get_preorder_list()
        return preorder_list

# BinarySearchTree is a binary tree consisting of TreeNodes
class BinarySearchTree:
    # init the BinarySearchTree
    def __init__(self): # Returns empty BST
        self.root = None

    # Checks if the root is empty, returns True if tree is empty, else False
    # returns a boolean
    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    # Searches for a given key in the tree, returns True if key is in a node of the tree, else False
    # returns a boolean
    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        current = self.root
        while current != None:
            if current.key == key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    # Inserts new node w/ key and data. If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data, returns True once inserted
    # key is an int
    # data is an int or None if not specified
    # returns a boolean
    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.is_empty():
            self.root = TreeNode(key, data)
            return True
        current = self.root
        while current != None:
            if current.key == key:
                current.data = data
                return True
            elif current.key < key:
                if current.right == None:
                    current.right = TreeNode(key, data)
                    return True
                current = current.right
            else:
                if current.left == None:
                    current.left = TreeNode(key, data)
                    return True
                current = current.left

    # Finds the minimum(leftmost) node in the tree and returns a tuple containing min key and data
    # returns a tuple or None if tree is empty
    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        current = self.root
        while current.left != None:
            current = current.left
        return (current.key, current.data)

    # Finds the minimum(rightmost) node in the tree and returns a tuple containing max key and data
    # returns a tuple or None if tree is empty
    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        current = self.root
        while current.right != None:
            current = current.right
        return (current.key, current.data)

    # Finds and returns the height of the BinarySearchTree
    # returns an int or None if tree is empty
    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return self.root.get_height(self.root)

    # Uses helper function get_inorder_list to recursively make and return an inorder list
    # It is the in-order traversal of the BST
    # returns a list
    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.is_empty():
            return []
        return self.root.get_inorder_list()

    # Uses helper function get_preorder_list to recursively make and return a preorder list
    # It is the pre-order traversal of the BST
    # returns a list
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty():
            return []
        return self.root.get_preorder_list()
        
    # Recursively makes and returns a levelorder list, representing level-order traversal of BST
    # returns a list
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        if self.is_empty():
            return []
        q.enqueue(self.root)
        level_list = []
        while not q.is_empty():
            this_node = q.dequeue()
            level_list.append(this_node.key)
            if this_node.left != None:
                q.enqueue(this_node.left)
            if this_node.right != None:
                q.enqueue(this_node.right)
        return level_list
