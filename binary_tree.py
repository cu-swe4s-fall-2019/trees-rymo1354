class Node:

    def __init__(self, key, value=None, left=None, right=None):
        """
        Creates a binary tree Node object
        Arguments
        _________
        key: key for the node, stored in self.key
        value: value for the node key, store in self.value
        left: left child node, initialized as None
        right: right child node, initialized as None
        """

        self.value = value
        self.left = left
        self.right = right
        self.key = key


class BinaryTree:

    def __init__(self):
        """
        Initializes BinaryTree object
        Arguments
        _________
        root: root of the tree, initialized as None
        """

        self.root = None

    def insert(self, key, value=None):
        """
        Inserts root node to BinaryTree object OR calls self.add
        Arguments
        _________
        key: key of a node to be created
        value: value of a node to be created
        Returns
        _______
        Nothing, just calls the add function
        """

        if self.root is None:
            self.root = Node(key, value)
        else:
            self.add(key, value, self.root)

    def add(self, key, value, node):
        """
        Adds node to BinaryTree object
        Arguments
        _________
        key: key of a node to be created
        value: value of a node to be created
        node: node to check (begins at root node)
        Returns
        _______
        Nothing, just performs the function calls.
        Function Calls:
        _______
        Adds nodes to left or right child of previous nodes,
        based upon the acceptance criteria.
        """

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
        """
        Locates node in BinaryTree object
        Arguments
        _________
        key: key of a node to locate
        Returns
        _______
        Self.find function if the root of the tree is not None
        """

        if self.root is None:
            return None
        else:
            return self.find(key, self.root)

    def find(self, key, node):
        """
        Adds node to BinaryTree object
        Arguments
        _________
        key: key of a node to be created
        node: node to check (begins at root node)
        Returns
        _______
        Node if a node with the given key is identified
        Function Calls:
        _______
        Walks through tree based on node key and children;
        finds the  node with the user-specified key
        """

        if key == node.key:
            return node
        elif node.right is None and node.left is None:
            return None
        elif key < node.key and node.left is not None:
            return self.find(key, node.left)
        elif key > node.key and node.right is not None:
            return self.find(key, node.right)
