import binary_tree
import unittest
import os


class TestBinaryTree(unittest.TestCase):
    def test_node(self):
        testnode = binary_tree.Node(1, 'test_value')
        self.assertEqual(testnode.key, 1)
        self.assertEqual(testnode.value, 'test_value')
        self.assertEqual(testnode.left, None)
        self.assertEqual(testnode.right, None)

    def test_binary_tree_insert(self):
        binarytree = binary_tree.BinaryTree()
        self.assertEqual(binarytree.root, None)
        binarytree.insert(5, 'test_value')
        self.assertEqual(binarytree.root.key, 5)
        self.assertEqual(binarytree.root.value, 'test_value')

    def test_binary_tree_add(self):
        binarytree = binary_tree.BinaryTree()
        binarytree.insert(5, 'test_value')
        binarytree.insert(6, 'test_value_2')
        self.assertEqual(binarytree.root.right.key, 6)
        self.assertEqual(binarytree.root.right.value, 'test_value_2')
        binarytree.insert(5, 'test_value_3')
        self.assertEqual(binarytree.root.right.left.key, 5)
        self.assertEqual(binarytree.root.right.left.value, 'test_value_3')


if __name__ == '__main__':
    unittest.main()
