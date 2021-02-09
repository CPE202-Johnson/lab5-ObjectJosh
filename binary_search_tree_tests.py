import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty()) # is empty
        self.assertFalse(bst.search(10)) # search empty tree
        self.assertEqual(bst.find_min(), None) # finding min of empty tree
        self.assertEqual(bst.find_max(), None) # finding max of empty tree
        self.assertTrue(bst.insert(10, 'stuff')) # inserting to empty tree
        self.assertTrue(bst.search(10)) # successful search
        self.assertFalse(bst.search(1)) # not in tree
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        self.assertTrue(bst.insert(10, 'other'))
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])
        self.assertTrue(bst.insert(20, 'next'))
    
    def test_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        bst.insert(10, '1')
        bst.insert(10, '2')
        self.assertEqual(bst.root.get_height(bst.root), 0)
        self.assertEqual(bst.tree_height(), 0)
        bst.insert(20, '3')
        self.assertEqual(bst.root.get_height(bst.root), 1)
        self.assertEqual(bst.tree_height(), 1)
        bst.insert(30, '3')
        self.assertEqual(bst.root.get_height(bst.root), 2)
        self.assertEqual(bst.tree_height(), 2)
    
    def test_inorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(10, '1')
        bst.insert(10, '2')
        bst.insert(20, '3')
        bst.insert(30, '3')
        self.assertEqual(bst.root.get_inorder_list(), [10, 20, 30])
        self.assertEqual(bst.inorder_list(), [10, 20, 30])
    
    def test_preorder_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        bst.insert(10, '1')
        bst.insert(10, '2')
        bst.insert(20, '3')
        bst.insert(30, '3')
        self.assertEqual(bst.root.get_preorder_list(), [10, 20, 30])
        self.assertEqual(bst.preorder_list(), [10, 20, 30])
    
    def test_level_order_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.level_order_list(), [])
        bst.insert(10, '1')
        bst.insert(10, '2')
        bst.insert(20, '3')
        bst.insert(30, '3')
        self.assertEqual(bst.level_order_list(), [10, 20, 30])

if __name__ == '__main__': 
    unittest.main()
