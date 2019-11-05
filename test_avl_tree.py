import sys
import importlib
import unittest
import copy
sys.path.append('avl_tree')
avl = importlib.import_module('avl_tree.avl')  # noqa: E402


class TestAVLTree(unittest.TestCase):
    def test_node(self):
        testnode = avl.AVLNode(None, 10)
        self.assertEqual(testnode.key, 10)
        self.assertEqual(testnode.find(10), testnode)

    def test_avl_tree_insert_root(self):
        avltree = avl.AVL()
        self.assertEqual(avltree.__str__(), '<empty tree>')
        avltree.insert(10)
        self.assertEqual(avltree.find(10).parent, None)

    def test_avl_tree_insert_rebalance(self):
        avltree = avl.AVL()
        inserts = [0, 10, 20, 30, 40, 50]
        for key in inserts:
            avltree.insert(key)
        self.assertEqual(avltree.root.key, 30)
        self.assertEqual(avltree.find_min().key, 0)
        self.assertEqual(avltree.next_larger(40), avltree.find(50))
        print('Test tree with keys: 0, 10, 20, 30, 40, 50')
        print(avltree)

    def test_avl_tree_delete(self):
        avltree = avl.AVL()
        inserts = [0, 10, 20, 30, 40, 50]
        for key in inserts:
            avltree.insert(key)
        avltree.delete(20)
        self.assertEqual(avltree.find(20), None)


if __name__ == '__main__':
    unittest.main()
