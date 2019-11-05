class Node:

    def __init__(self, key, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.key = key


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.add(key, value, self.root)

    def add(self, key, value, node):
        if key < node.key:
            if node.left is not None:
                self.add(key, value, node.left)
            else:
                node.left = Node(key, value)
        else:
            if node.right is not None:
                self.add(key, value, node.right)
            else:
                node.right = Node(key, value)

    def search(self, key):
        pass
